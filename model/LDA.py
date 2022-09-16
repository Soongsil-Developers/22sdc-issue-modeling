from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer


def get_topics(components, feature_names, n=5):
    for idx, topic in enumerate(components):
        print(f"Topic {idx + 1}:{[(feature_names[i], topic[i].round(2)) for i in topic.argsort()[:-n - 1:-1]]}")


def lda_model(processed):
    vect = TfidfVectorizer(ngram_range=(1, 1), lowercase=True, tokenizer=lambda x: x.split(), max_features=500)
    input_matrix = vect.fit_transform(processed)
    terms = vect.get_feature_names_out()

    model = LatentDirichletAllocation()
    model.fit_transform(input_matrix)

    topic = []
    # get_topics(model.components_, terms)
    for comp in model.components_:
        idx = comp.argsort()[:-2:-1]
        topic.append(terms[idx].item())

    return topic
