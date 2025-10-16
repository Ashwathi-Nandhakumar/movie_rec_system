# Movie Recommendation System

## Project Overview
Discover your next favorite film!  
This smart movie recommender analyzes genres and plot summaries to suggest the most similar movies from a database of 10,000 titles—all in a single click through a sleek Streamlit interface.

## Dataset
- **File:** `top10K-TMDB-movies.csv`
- **Movies Covered:** 10,000+ from a wide range of genres
- **Key Information:** Title, genre, plot overview, language, release date, ratings
- **Engineered Feature:** "Tags" combines descriptive text and genres for next-level recommendations

## Workflow

1. **Data Preparation**
    - Clean and merge metadata
    - Generate unified "tags" for each movie

2. **Feature Extraction**
    - Apply NLP (`CountVectorizer`) to convert tags into a meaningful vector space
    - Eliminate irrelevant words with stop-word filtering

3. **Similarity Calculation**
    - Use cosine similarity to score movie pairs and surface the closest matches

4. **Recommendation Engine**
    - Instantly retrieves the top 5 most similar films for any selected title

5. **Streamlit Deployment**
    - Engaging UI for fast, interactive movie discovery

## Results

- **Spot-on similarity suggestions**—find films you'll love, even before you know it!
- **Lightning-fast search** with pre-computed data for an instant user experience
- **No ratings or user profiles needed**—purely content-based recommendations, ideal for new and diverse audiences

***

*This project showcases practical NLP and content-based filtering for real-world entertainment discovery. Explore, enjoy, and expand your movie universe!*

