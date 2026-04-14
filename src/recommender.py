from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    
    Returns a list of dictionaries, each representing a song.
    """
    print(f"Loading songs from {csv_path}...")
    try:
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            songs = []
            for row in reader:
                song_dict = {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"])
                }
                songs.append(song_dict)
            return songs
    except FileNotFoundError:
        return []
    


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Returns a (score, reasons) tuple where score is between 0 and 1.
    """
    
    # Should be changed so that its more adaptable when the list of songs increase. 
    ENERGY_RANGE      = 0.77
    TEMPO_RANGE       = 123
    DANCEABILITY_RANGE = 0.72

    score = 0.0
    reasons = []

    # Genre match (+0.30)
    if user_prefs["favorite_genre"] == song["genre"]:
        score += 0.30
        reasons.append("Genre match (+0.30)")
    else:
        reasons.append("Genre mismatch (0)")

    # Mood match (+0.25)
    if user_prefs["favorite_mood"] == song["mood"]:
        score += 0.25
        reasons.append("Mood match (+0.25)")
    else:
        reasons.append("Mood mismatch (0)")

    # Energy similarity (up to +0.20)
    energy_sim = max(0.0, 1 - abs(user_prefs["target_energy"] - song["energy"]) / ENERGY_RANGE)
    energy_points = round(0.20 * energy_sim, 3)
    score += energy_points
    reasons.append(f"Energy similarity: {round(energy_sim, 2)} similarity (+{energy_points})")

    # Tempo similarity (up to +0.15)
    target_tempo = user_prefs.get("target_tempo", 120)
    tempo_sim = max(0.0, 1 - abs(target_tempo - song["tempo_bpm"]) / TEMPO_RANGE)
    tempo_points = round(0.15 * tempo_sim, 3)
    score += tempo_points
    reasons.append(f"Tempo similarity: {round(tempo_sim, 2)} similarity (+{tempo_points})")

    # Danceability similarity (up to +0.10)
    target_dance = user_prefs.get("target_danceability", 0.70)
    dance_sim = max(0.0, 1 - abs(target_dance - song["danceability"]) / DANCEABILITY_RANGE)
    dance_points = round(0.10 * dance_sim, 3)
    score += dance_points
    reasons.append(f"Danceability similarity: {round(dance_sim, 2)} similarity (+{dance_points})")

    score = round(score, 3)
    reasons.append(f"Total score: {score}/1.0")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # If the user started from a specific song (seed), grab its id so we can skip it.
    # .get() returns None safely if "seed_id" isn't in user_prefs.
    seed_id = user_prefs.get("seed_id")

    results = []
    for song in songs:
        # Don't recommend the seed song back to the user
        if song["id"] == seed_id:
            continue

        # score_song returns two values; we unpack them directly into two variables
        score, reasons = score_song(user_prefs, song)

        # reasons is a List[str] — join them into one readable string separated by " | "
        explanation = " | ".join(reasons)

        # Each result is a 3-item tuple matching the return type: (song, score, explanation)
        results.append((song, score, explanation))

    # sorted() returns a NEW list ranked by score.
    # key=lambda x: x[1] tells sorted() what to compare:
    #   x is one tuple from results, e.g. (song_dict, 0.85, "Genre match | ...")
    #   x[1] picks the score (index 1), so songs are ranked by score, not by song_dict or explanation.
    # reverse=True means highest score first (descending order).
    # [:k] slices off just the top k results.
    return sorted(results, key=lambda x: x[1], reverse=True)[:k]
