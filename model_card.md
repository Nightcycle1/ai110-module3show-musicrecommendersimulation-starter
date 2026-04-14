# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

VibeMatcher 1.0

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration

This recommender suggests 5 songs from a small dataset based on a user's favorite song. It assumes the user wants songs that sound similar in genre, mood, energy, tempo and danceability. This is classroom exploration only, not real users.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The system starts with a seed song the user loves. It then scores every other song in the dataset using five rules: genre match (30%), mood match (25%), energy similarity (20%), tempo similarity (15%), and danceability similarity (10%). Songs with matching genres or moods get big bonuses. For energy, tempo, and danceability, the system measures how close the numbers are. The top 5 highest-scoring songs become the recommendations.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The dataset has 20 songs across 16 genres and 16 moods. Genres include pop, lofi, rock, metal, classical, electronic, hip hop, and reggae. I added 10 new songs to the original 10 to increase diversity. However, 13 genres appear only once, so niche tastes like metal are underrepresented.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works well for users who like popular genres with multiple songs, like lofi (3 songs) or pop (2 songs). It correctly matches "Chill Lofi" users with low-energy, slow-tempo songs. The scoring is transparent, every point is explained, so users know why a song was recommended.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

**Genre Underrepresentation:** My dataset has 13 genres that appear only once, including metal, classical, and reggae. A user who loves metal receives only one possible genre match ("Thunder Beast"), and since that song is excluded as the seed, they get zero genre-matched recommendations. In contrast, a lofi user has three songs to choose from and consistently fills their top 5 with genre matches. This creates an unfair advantage for users of overrepresented genres and fails users with niche tastes.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.


I tested five distinct user profiles to evaluate how my recommender behaves across different musical tastes:

| Profile              | Seed Song       | Genre      | Mood       | Energy | Tempo | Key Test                  |
| -------------------- | --------------- | ---------- | ---------- | ------ | ----- | ------------------------- |
| 1. High-Energy Pop   | Sunrise City    | pop        | happy      | 0.82   | 118   | Balanced preferences      |
| 2. Chill Lofi        | Midnight Coding | lofi       | chill      | 0.42   | 78    | Low energy, relaxed       |
| 3. Deep Intense Rock | Storm Runner    | rock       | intense    | 0.91   | 152   | High energy, fast tempo   |
| 4. Sad/Angry Metal   | Thunder Beast   | metal      | aggressive | 0.95   | 175   | Minority genre, rare mood |
| 5. Contradictory     | Club Paradox    | electronic | sad        | 0.89   | 126   | Conflicting preferences   |

For each profile, I examined:
- Whether the top recommendations matched the user's genre and mood when possible
- How the system handled profiles with rare or missing genre/mood combinations
- Whether continuous features (energy, tempo, danceability) could compensate when labels didn't match
- If the seed song was properly excluded from results


**Test 1: Weight Swap Experiment.** I swapped genre (0.30 → 0.20) and energy (0.20 → 0.30) weights. For Profile 1, the top recommendation changed from "Gym Hero" (genre match) to "Rooftop Lights" (energy match). This proved the system is sensitive to weight changes and that energy similarity can overcome genre mismatch when weighted properly.


---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  


- Calculate feature range dynamically instead of hardcoding them
- Support multiple liked songs instead of just one seed song

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

Building this content-based recommender has given me insight into how recommendation algorithms work via scoring and ranking. The weighted additive formula used is simple yet produced reasonable outcomes. In terms of things I have found interesting or unexpected that may include is you may not get the results you want with small datasets, in my case only 20 songs. Overall this project has given me insight into large music platforms may be using many more weights in their recommendation algorithms that I may not have accounted for like time of day. 

