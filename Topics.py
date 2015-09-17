from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

documents = ["You have to see what Bradley Cooper does in this movie. His performance is next level"
              "Bradley Cooper killed that role in American Sniper. Mad respect"
             " He's proper buzzing  loves Bradley Cooper"
             "Bradley Cooper is awesome in" 
             "ChrisKyle TheLegend is a hero Hooyah ChrisKyleFrog ",
             "Chris Kyle's widow: I will miss him every single day of my life",
             "Before you watch AmericanSniper, hear about Chris Kyles fight for freedom "
             "Why are leftists offended by America Sniper Chris dKyle calling the enemy savages not as offended by tweets",
             "Chris Kyle his country most of us couldn't do.  Honor him by insuring what we ask has honor.",
             "Chris Kyle wasn't the slightest bit of a hero",
             "Chris Kyle defines the word hero",
             "I still can not get over how sexy Bradley Cooper is in American Sniper",
             "you should know one thing. Bradley Cooper is a good dude who really cares about vets"]
print type(documents)
true_k = 2
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print "Cluster %d:" % i,
    for ind in order_centroids[i, :10]:
        print ' %s' % terms[ind],
    print
