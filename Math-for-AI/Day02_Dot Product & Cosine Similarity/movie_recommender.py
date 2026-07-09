import math
from cosine_similarity import cosine_similarity
user = [0.9, 0.3, 0.1]
max_similarity=0
best_movie=-1
movie1 = [0.8, 0.2, 0.1]   # Action movie
movie2 = [0.4, 0.9, 0.3]   # Comedy movie
movie3 = [0.2, 0.2, 0.9]   # Romance movie
movie4 = [0.7, 0.4, 0.2]   # Action + Comedy
movies=[movie1,movie2,movie3,movie4]
for i, movie in enumerate(movies, start=1):
    similarity = cosine_similarity(user, movie)
    print(f"Movie {i}: {similarity:.3f}")

    if similarity > max_similarity:
        max_similarity = similarity
        best_movie = i
print(f"Recomended Movie:Movie {best_movie}")