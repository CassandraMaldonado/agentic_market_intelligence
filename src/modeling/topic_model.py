from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


def extract_topics(texts: list[str], n_topics: int = 3, n_words: int = 5) -> list[list[str]]:
    vectorizer = CountVectorizer(stop_words="english", min_df=1)
    matrix = vectorizer.fit_transform(texts)

    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda.fit(matrix)

    words = vectorizer.get_feature_names_out()
    topics = []

    for topic in lda.components_:
        top_indices = topic.argsort()[-n_words:][::-1]
        topics.append([words[i] for i in top_indices])

    return topics
