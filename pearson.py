from controller import get_users, get_object

def get_pearson(users):
    scores = {}
    for user in users:
        scores[user] = get_score(user)
    return scores


def get_score(user):
    # get the ratings for this user
    ratings = get_users()[user]
    # get the mean
    mean = get_mean(ratings)
    # calculate the pearson score
    n = 0
    num = 0
    dem = 0
    for item in ratings:
        n += 1
        num += (ratings[item] - mean) * (get_users()[user][item] - mean)
        dem += (ratings[item] - mean) ** 2
    return num / (dem ** 0.5)

def get_mean(ratings):
    n = 0
    sum = 0
    for item in ratings:
        n += 1
        sum += ratings[item]
    return sum / n
 
def get_recommendation(user):
    # get the pearson score
    scores = get_pearson(get_users())
    # get the top 10
    ranked = get_top_matches(scores, user)
    #get the items
    items = get_object()
    # get the recommendations
    recommendations = {}
    for (person, score) in ranked:
        for item in items:
            if item not in get_users()[person]:
                if item not in recommendations:
                    recommendations[item] = (score, person)
    # sort the recommendations
    recommendations = sorted(recommendations.items(), key=lambda x: x[1][0], reverse=True)
    return recommendations
 
def get_top_matches(scores, user):
    ranked = []
    for person in scores:
        if person != user:
            ranked.append((person, scores[person]))
