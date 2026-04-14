# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

My recommendation system uses content-based filtering. It recommeneds songs based soley on how similar they are to a song the user already loves. So unlike Spotify or Youtube music, this simulation does not use date from other uses (collaboritive filtering) or contextual signals like time of day. Instead it focuses entirely on the music al attributes of each track. I decided on this system based on how easier it would be compared to implimenting other filtering. 


| Feature        | Type         | What It Means                                                |
| -------------- | ------------ | ------------------------------------------------------------ |
| `genre`        | Category     | The musical style (pop, rock, lofi, synthwave, metal, etc.)  |
| `mood`         | Category     | The emotional feel (happy, chill, intense, moody, sad, etc.) |
| `energy`       | Number (0-1) | How intense and active the song sounds                       |
| `tempo_bpm`    | Number       | Beats per minute — the speed of the song                     |
| `danceability` | Number (0-1) | How suitable the song is for dancing                         |

*Note: The dataset also includes `valence` and `acousticness`, but I chose not to use them to keep the system simple and focused.*

A `UserProfile` stores the musical preferences of a listener. For this simulation, a profile is created from a **seed song** — a track the user already loves:

```python
user_profile = {
    "favorite_genre": "synthwave",     # from seed song
    "favorite_mood": "moody",          # from seed song
    "target_energy": 0.72,             # from seed song
    "target_tempo": 108,               # from seed song (BPM)
    "target_danceability": 0.70        # from seed song
}
```
```
The recommender uses a weighted additive formula. Every song gets a score between 0 and 1:

Score = (genre_match × 0.30) + (mood_match × 0.25) 
      + (energy_similarity × 0.20) 
      + (tempo_similarity × 0.15) 
      + (danceability_similarity × 0.10)

For energy, tempo, and danceability, similarity is calculated as:

`similarity = 1 - (|target_value - song_value| ÷ feature_range)`

The **feature_range** is the difference between the maximum and minimum values in the dataset (e.g., energy ranges from 0.18 to 0.95, so range = 0.77).

After every song in the dataset gets a score, the recommender:

- Sorts all songs by score from highest to lowest

- Filters out the seed song itself (can't recommend what they already love)

- Returns the top K recommendations (default K = 5)



---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

### Experiment 1: Testing Diverse User Profiles

I tested 5 different user profiles to see how my recommender behaves across different musical tastes. The full results are shown above.

**What I learned:** Users with popular genres (pop, lofi) get better recommendations because more songs match their preferences. Users with niche tastes (metal, aggressive mood) get fewer matches and lower scores.

### Experiment 2: Swapping Genre and Energy Weights

I changed the weights from:
- Genre: 0.30, Energy: 0.20

To:
- Genre: 0.20, Energy: 0.30

**What changed:** For Profile 1 (High-Energy Pop), the top recommendation switched from "Gym Hero" (genre match) to "Rooftop Lights" (energy match). This proves the system is sensitive to weight changes — higher energy weight prioritizes songs that sound similar over songs that share a genre label.

---

**Before Experiment (Genre 0.30, Energy 0.20):**

Loading songs from data/songs.csv...


PROFILE 1: High-Energy Pop -- Top 5 Results        


#1  Gym Hero by Max Pulse
    Genre: pop | Mood: intense | Tempo: 132 BPM
    Match Score: 0.692 / 1.000

    Why this song?
      - Genre match (+0.30)
      - Mood mismatch (0)
      - Energy similarity: 0.86 similarity (+0.171)
      - Tempo similarity: 0.89 similarity (+0.133)
      - Danceability similarity: 0.88 similarity (+0.088)
      - Total score: 0.692/1.0


#2  Rooftop Lights by Indigo Parade
    Genre: indie pop | Mood: happy | Tempo: 124 BPM
    Match Score: 0.673 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood match (+0.25)
      - Energy similarity: 0.92 similarity (+0.184)
      - Tempo similarity: 0.95 similarity (+0.143)
      - Danceability similarity: 0.96 similarity (+0.096)
      - Total score: 0.673/1.0


#3  Night Drive Loop by Neon Echo
    Genre: synthwave | Mood: moody | Tempo: 110 BPM
    Match Score: 0.414 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.91 similarity (+0.182)
      - Tempo similarity: 0.93 similarity (+0.14)
      - Danceability similarity: 0.92 similarity (+0.092)
      - Total score: 0.414/1.0


#4  Neon Tokyo by Kitsune Beats
    Genre: electronic | Mood: energetic | Tempo: 128 BPM
    Match Score: 0.408 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.94 similarity (+0.187)
      - Tempo similarity: 0.92 similarity (+0.138)
      - Danceability similarity: 0.83 similarity (+0.083)
      - Total score: 0.408/1.0


#5  Street Fighter by Rival Beats
    Genre: hip hop | Mood: confident | Tempo: 94 BPM
    Match Score: 0.407 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.96 similarity (+0.192)
      - Tempo similarity: 0.8 similarity (+0.121)
      - Danceability similarity: 0.94 similarity (+0.094)
      - Total score: 0.407/1.0



PROFILE 2: Chill Lofi -- Top 5 Results


#1  Library Rain by Paper Lanterns
    Genre: lofi | Mood: chill | Tempo: 72 BPM
    Match Score: 0.969 / 1.000

    Why this song?
      - Genre match (+0.30)
      - Mood match (+0.25)
      - Energy similarity: 0.91 similarity (+0.182)
      - Tempo similarity: 0.95 similarity (+0.143)
      - Danceability similarity: 0.94 similarity (+0.094)
      - Total score: 0.969/1.0


#2  Focus Flow by LoRoom
    Genre: lofi | Mood: focused | Tempo: 80 BPM
    Match Score: 0.740 / 1.000

    Why this song?
      - Genre match (+0.30)
      - Mood mismatch (0)
      - Energy similarity: 0.97 similarity (+0.195)
      - Tempo similarity: 0.98 similarity (+0.148)
      - Danceability similarity: 0.97 similarity (+0.097)
      - Total score: 0.74/1.0


#3  Spacewalk Thoughts by Orbit Bloom
    Genre: ambient | Mood: chill | Tempo: 60 BPM
    Match Score: 0.613 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood match (+0.25)
      - Energy similarity: 0.82 similarity (+0.164)
      - Tempo similarity: 0.85 similarity (+0.128)
      - Danceability similarity: 0.71 similarity (+0.071)
      - Total score: 0.613/1.0


#4  Coffee Shop Stories by Slow Stereo
    Genre: jazz | Mood: relaxed | Tempo: 90 BPM
    Match Score: 0.411 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.94 similarity (+0.187)
      - Tempo similarity: 0.9 similarity (+0.135)
      - Danceability similarity: 0.89 similarity (+0.089)
      - Total score: 0.411/1.0


#5  Desert Highway by The Dusty Boots
    Genre: folk | Mood: hopeful | Tempo: 96 BPM
    Match Score: 0.396 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.84 similarity (+0.169)
      - Tempo similarity: 0.85 similarity (+0.128)
      - Danceability similarity: 0.99 similarity (+0.099)
      - Total score: 0.396/1.0


PROFILE 3: Deep Intense Rock -- Top 5 Results


#1  Gym Hero by Max Pulse
    Genre: pop | Mood: intense | Tempo: 132 BPM
    Match Score: 0.640 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood match (+0.25)
      - Energy similarity: 0.97 similarity (+0.195)
      - Tempo similarity: 0.84 similarity (+0.126)
      - Danceability similarity: 0.69 similarity (+0.069)
      - Total score: 0.64/1.0


#2  Cyber Wasteland by NullSignal
    Genre: industrial | Mood: angry | Tempo: 160 BPM
    Match Score: 0.413 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.96 similarity (+0.192)
      - Tempo similarity: 0.93 similarity (+0.14)
      - Danceability similarity: 0.81 similarity (+0.081)
      - Total score: 0.413/1.0


#3  Thunder Beast by Iron Maw
    Genre: metal | Mood: aggressive | Tempo: 175 BPM
    Match Score: 0.383 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.95 similarity (+0.19)
      - Tempo similarity: 0.81 similarity (+0.122)
      - Danceability similarity: 0.71 similarity (+0.071)
      - Total score: 0.383/1.0


#4  Neon Tokyo by Kitsune Beats
    Genre: electronic | Mood: energetic | Tempo: 128 BPM
    Match Score: 0.376 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.95 similarity (+0.19)
      - Tempo similarity: 0.8 similarity (+0.121)
      - Danceability similarity: 0.65 similarity (+0.065)
      - Total score: 0.376/1.0


#5  Club Paradox by DJ Phantom
    Genre: house | Mood: euphoric | Tempo: 126 BPM
    Match Score: 0.374 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.97 similarity (+0.195)
      - Tempo similarity: 0.79 similarity (+0.118)
      - Danceability similarity: 0.61 similarity (+0.061)
      - Total score: 0.374/1.0



PROFILE 4: Sad/Angry Metal -- Top 5 Results


#1  Cyber Wasteland by NullSignal
    Genre: industrial | Mood: angry | Tempo: 160 BPM
    Match Score: 0.419 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.99 similarity (+0.197)
      - Tempo similarity: 0.88 similarity (+0.132)
      - Danceability similarity: 0.9 similarity (+0.09)
      - Total score: 0.419/1.0


#2  Storm Runner by Voltline
    Genre: rock | Mood: intense | Tempo: 152 BPM
    Match Score: 0.383 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.95 similarity (+0.19)
      - Tempo similarity: 0.81 similarity (+0.122)
      - Danceability similarity: 0.71 similarity (+0.071)
      - Total score: 0.383/1.0


#3  Gym Hero by Max Pulse
    Genre: pop | Mood: intense | Tempo: 132 BPM
    Match Score: 0.333 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.97 similarity (+0.195)
      - Tempo similarity: 0.65 similarity (+0.098)
      - Danceability similarity: 0.4 similarity (+0.04)
      - Total score: 0.333/1.0


#4  Neon Tokyo by Kitsune Beats
    Genre: electronic | Mood: energetic | Tempo: 128 BPM
    Match Score: 0.308 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.9 similarity (+0.179)
      - Tempo similarity: 0.62 similarity (+0.093)
      - Danceability similarity: 0.36 similarity (+0.036)
      - Total score: 0.308/1.0


#5  Club Paradox by DJ Phantom
    Genre: house | Mood: euphoric | Tempo: 126 BPM
    Match Score: 0.306 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.92 similarity (+0.184)
      - Tempo similarity: 0.6 similarity (+0.09)
      - Danceability similarity: 0.32 similarity (+0.032)
      - Total score: 0.306/1.0



PROFILE 5: Contradictory (High Energy + Sad Mood) -- Top 5 Results


#1  Neon Tokyo by Kitsune Beats
    Genre: electronic | Mood: energetic | Tempo: 128 BPM
    Match Score: 0.743 / 1.000

    Why this song?
      - Genre match (+0.30)
      - Mood mismatch (0)
      - Energy similarity: 0.97 similarity (+0.195)
      - Tempo similarity: 0.98 similarity (+0.148)
      - Danceability similarity: 1.0 similarity (+0.1)
      - Total score: 0.743/1.0


#2  Gym Hero by Max Pulse
    Genre: pop | Mood: intense | Tempo: 132 BPM
    Match Score: 0.429 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.95 similarity (+0.19)
      - Tempo similarity: 0.95 similarity (+0.143)
      - Danceability similarity: 0.96 similarity (+0.096)
      - Total score: 0.429/1.0


#3  Sunrise City by Neon Echo
    Genre: pop | Mood: happy | Tempo: 118 BPM
    Match Score: 0.405 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.91 similarity (+0.182)
      - Tempo similarity: 0.93 similarity (+0.14)
      - Danceability similarity: 0.83 similarity (+0.083)
      - Total score: 0.405/1.0


#4  Silent Tears by Echo Chamber
    Genre: country | Mood: sad | Tempo: 68 BPM
    Match Score: 0.404 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood match (+0.25)
      - Energy similarity: 0.25 similarity (+0.049)
      - Tempo similarity: 0.53 similarity (+0.079)
      - Danceability similarity: 0.26 similarity (+0.026)
      - Total score: 0.404/1.0


#5  Rooftop Lights by Indigo Parade
    Genre: indie pop | Mood: happy | Tempo: 124 BPM
    Match Score: 0.401 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.83 similarity (+0.166)
      - Tempo similarity: 0.98 similarity (+0.148)
      - Danceability similarity: 0.87 similarity (+0.087)
      - Total score: 0.401/1.0



**After Experiment (Genre 0.20, Energy 0.30):**

Loading songs from data/songs.csv...


PROFILE 1: High-Energy Pop -- Top 5 Results        


#1  Rooftop Lights by Indigo Parade
    Genre: indie pop | Mood: happy | Tempo: 124 BPM
    Match Score: 0.766 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood match (+0.25)
      - Energy similarity: 0.92 similarity (+0.277)
      - Tempo similarity: 0.95 similarity (+0.143)
      - Danceability similarity: 0.96 similarity (+0.096)
      - Total score: 0.766/1.0

#2  Gym Hero by Max Pulse
    Genre: pop | Mood: intense | Tempo: 132 BPM
    Match Score: 0.678 / 1.000

    Why this song?
      - Genre match (+0.20)
      - Mood mismatch (0)
      - Energy similarity: 0.86 similarity (+0.257)
      - Tempo similarity: 0.89 similarity (+0.133)
      - Danceability similarity: 0.88 similarity (+0.088)
      - Total score: 0.678/1.0


#3  Night Drive Loop by Neon Echo
    Genre: synthwave | Mood: moody | Tempo: 110 BPM
    Match Score: 0.505 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.91 similarity (+0.273)
      - Tempo similarity: 0.93 similarity (+0.14)
      - Danceability similarity: 0.92 similarity (+0.092)
      - Total score: 0.505/1.0


#4  Street Fighter by Rival Beats
    Genre: hip hop | Mood: confident | Tempo: 94 BPM
    Match Score: 0.503 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.96 similarity (+0.288)
      - Tempo similarity: 0.8 similarity (+0.121)
      - Danceability similarity: 0.94 similarity (+0.094)
      - Total score: 0.503/1.0


#5  Neon Tokyo by Kitsune Beats
    Genre: electronic | Mood: energetic | Tempo: 128 BPM
    Match Score: 0.502 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.94 similarity (+0.281)
      - Tempo similarity: 0.92 similarity (+0.138)
      - Danceability similarity: 0.83 similarity (+0.083)
      - Total score: 0.502/1.0



PROFILE 2: Chill Lofi -- Top 5 Results


#1  Library Rain by Paper Lanterns
    Genre: lofi | Mood: chill | Tempo: 72 BPM
    Match Score: 0.960 / 1.000

    Why this song?
      - Genre match (+0.20)
      - Mood match (+0.25)
      - Energy similarity: 0.91 similarity (+0.273)
      - Tempo similarity: 0.95 similarity (+0.143)
      - Danceability similarity: 0.94 similarity (+0.094)
      - Total score: 0.96/1.0


#2  Focus Flow by LoRoom
    Genre: lofi | Mood: focused | Tempo: 80 BPM
    Match Score: 0.737 / 1.000

    Why this song?
      - Genre match (+0.20)
      - Mood mismatch (0)
      - Energy similarity: 0.97 similarity (+0.292)
      - Tempo similarity: 0.98 similarity (+0.148)
      - Danceability similarity: 0.97 similarity (+0.097)
      - Total score: 0.737/1.0


#3  Spacewalk Thoughts by Orbit Bloom
    Genre: ambient | Mood: chill | Tempo: 60 BPM
    Match Score: 0.694 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood match (+0.25)
      - Energy similarity: 0.82 similarity (+0.245)
      - Tempo similarity: 0.85 similarity (+0.128)
      - Danceability similarity: 0.71 similarity (+0.071)
      - Total score: 0.694/1.0


#4  Coffee Shop Stories by Slow Stereo
    Genre: jazz | Mood: relaxed | Tempo: 90 BPM
    Match Score: 0.505 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.94 similarity (+0.281)
      - Tempo similarity: 0.9 similarity (+0.135)
      - Danceability similarity: 0.89 similarity (+0.089)
      - Total score: 0.505/1.0


#5  Desert Highway by The Dusty Boots
    Genre: folk | Mood: hopeful | Tempo: 96 BPM
    Match Score: 0.480 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.84 similarity (+0.253)
      - Tempo similarity: 0.85 similarity (+0.128)
      - Danceability similarity: 0.99 similarity (+0.099)
      - Total score: 0.48/1.0



PROFILE 3: Deep Intense Rock -- Top 5 Results

#1  Gym Hero by Max Pulse
    Genre: pop | Mood: intense | Tempo: 132 BPM
    Match Score: 0.737 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood match (+0.25)
      - Energy similarity: 0.97 similarity (+0.292)
      - Tempo similarity: 0.84 similarity (+0.126)
      - Danceability similarity: 0.69 similarity (+0.069)
      - Total score: 0.737/1.0


#2  Cyber Wasteland by NullSignal
    Genre: industrial | Mood: angry | Tempo: 160 BPM
    Match Score: 0.509 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.96 similarity (+0.288)
      - Tempo similarity: 0.93 similarity (+0.14)
      - Danceability similarity: 0.81 similarity (+0.081)
      - Total score: 0.509/1.0


#3  Thunder Beast by Iron Maw
    Genre: metal | Mood: aggressive | Tempo: 175 BPM
    Match Score: 0.477 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.95 similarity (+0.284)
      - Tempo similarity: 0.81 similarity (+0.122)
      - Danceability similarity: 0.71 similarity (+0.071)
      - Total score: 0.477/1.0


#4  Club Paradox by DJ Phantom
    Genre: house | Mood: euphoric | Tempo: 126 BPM
    Match Score: 0.471 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.97 similarity (+0.292)
      - Tempo similarity: 0.79 similarity (+0.118)
      - Danceability similarity: 0.61 similarity (+0.061)
      - Total score: 0.471/1.0

#5  Neon Tokyo by Kitsune Beats
    Genre: electronic | Mood: energetic | Tempo: 128 BPM
    Match Score: 0.470 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.95 similarity (+0.284)
      - Tempo similarity: 0.8 similarity (+0.121)
      - Danceability similarity: 0.65 similarity (+0.065)
      - Total score: 0.47/1.0



PROFILE 4: Sad/Angry Metal -- Top 5 Results


#1  Cyber Wasteland by NullSignal
    Genre: industrial | Mood: angry | Tempo: 160 BPM
    Match Score: 0.518 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.99 similarity (+0.296)
      - Tempo similarity: 0.88 similarity (+0.132)
      - Danceability similarity: 0.9 similarity (+0.09)
      - Total score: 0.518/1.0


#2  Storm Runner by Voltline
    Genre: rock | Mood: intense | Tempo: 152 BPM
    Match Score: 0.477 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.95 similarity (+0.284)
      - Tempo similarity: 0.81 similarity (+0.122)
      - Danceability similarity: 0.71 similarity (+0.071)
      - Total score: 0.477/1.0


#3  Gym Hero by Max Pulse
    Genre: pop | Mood: intense | Tempo: 132 BPM
    Match Score: 0.430 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.97 similarity (+0.292)
      - Tempo similarity: 0.65 similarity (+0.098)
      - Danceability similarity: 0.4 similarity (+0.04)
      - Total score: 0.43/1.0


#4  Club Paradox by DJ Phantom
    Genre: house | Mood: euphoric | Tempo: 126 BPM
    Match Score: 0.399 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.92 similarity (+0.277)
      - Tempo similarity: 0.6 similarity (+0.09)
      - Danceability similarity: 0.32 similarity (+0.032)
      - Total score: 0.399/1.0


#5  Neon Tokyo by Kitsune Beats
    Genre: electronic | Mood: energetic | Tempo: 128 BPM
    Match Score: 0.398 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.9 similarity (+0.269)
      - Tempo similarity: 0.62 similarity (+0.093)
      - Danceability similarity: 0.36 similarity (+0.036)
      - Total score: 0.398/1.0



PROFILE 5: Contradictory (High Energy + Sad Mood) -- Top 5 Results


#1  Neon Tokyo by Kitsune Beats
    Genre: electronic | Mood: energetic | Tempo: 128 BPM
    Match Score: 0.740 / 1.000

    Why this song?
      - Genre match (+0.20)
      - Mood mismatch (0)
      - Energy similarity: 0.97 similarity (+0.292)
      - Tempo similarity: 0.98 similarity (+0.148)
      - Danceability similarity: 1.0 similarity (+0.1)
      - Total score: 0.74/1.0


#2  Gym Hero by Max Pulse
    Genre: pop | Mood: intense | Tempo: 132 BPM
    Match Score: 0.523 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.95 similarity (+0.284)
      - Tempo similarity: 0.95 similarity (+0.143)
      - Danceability similarity: 0.96 similarity (+0.096)
      - Total score: 0.523/1.0

#3  Sunrise City by Neon Echo
    Genre: pop | Mood: happy | Tempo: 118 BPM
    Match Score: 0.496 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.91 similarity (+0.273)
      - Tempo similarity: 0.93 similarity (+0.14)
      - Danceability similarity: 0.83 similarity (+0.083)
      - Total score: 0.496/1.0

#4  Rooftop Lights by Indigo Parade
    Genre: indie pop | Mood: happy | Tempo: 124 BPM
    Match Score: 0.484 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.83 similarity (+0.249)
      - Tempo similarity: 0.98 similarity (+0.148)
      - Danceability similarity: 0.87 similarity (+0.087)
      - Total score: 0.484/1.0

#5  Storm Runner by Voltline
    Genre: rock | Mood: intense | Tempo: 152 BPM
    Match Score: 0.475 / 1.000

    Why this song?
      - Genre mismatch (0)
      - Mood mismatch (0)
      - Energy similarity: 0.97 similarity (+0.292)
      - Tempo similarity: 0.79 similarity (+0.118)
      - Danceability similarity: 0.65 similarity (+0.065)
      - Total score: 0.475/1.0



## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.


- **Tiny catalog:** Only 20 songs
- **Genre imbalance:** 13 genres appear only once, metal fans get fewer matches than lofi fans
- **No mood diversity:** 10 moods appear only once, if the seed song has a rare mood, users get zero mood matches
- **Hardcoded ranges:** Feature ranges are based on the current 20 songs, adding extreme songs would break similarity calculations
- **No lyrics or culture:** The system can't understand that a sad song might still be enjoyable

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

Building this content-based recommender has given me insight into how recommendation algorithms work via scoring and ranking. The weighted additive formula used is simple yet produced reasonable outcomes. In terms of things I have found interesting or unexpected that may include is you may not get the results you want with small datasets, in my case only 20 songs. Overall this project has given me insight into large music platforms may be using many more weights in their recommendation algorithms that I may not have accounted for like time of day. 

---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

