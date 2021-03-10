def getUrl(mode,units):
    baseUrl ="https://api.openweathermap.org/data/2.5/"
    baseUrl +=mode+"?units="+units+"&appid=3612d28da84959d707e358c982572d6f&q="

    return baseUrl