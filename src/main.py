"""
main.py
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def print_recommendations(recommendations: list, k: int) -> None:
    """Prints the recommendation results in a clean, readable layout."""
    width = 60
    print("\n" + "=" * width)
    print(f"  Music Recommender -- Top {k} Results")
    print("=" * width)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']} by {song['artist']}")
        print(f"    Genre: {song['genre']} | Mood: {song['mood']} | Tempo: {int(song['tempo_bpm'])} BPM")
        print(f"    Match Score: {score:.3f} / 1.000")
        print()
        print("    Why this song?")
        # explanation is reasons joined by " | " — split to print each on its own line
        for reason in explanation.split(" | "):
            print(f"      - {reason}")
        print("-" * width)


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Keys must match what score_song expects: favorite_genre, favorite_mood, target_energy
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.82,
        "target_tempo": 118,    
        "target_danceability": 0.79,
        "seed_id": 1,
    }

    k = 5
    recommendations = recommend_songs(user_prefs, songs, k=k)
    print_recommendations(recommendations, k)


if __name__ == "__main__":
    main()
