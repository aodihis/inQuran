# Data Source
- [api.alquran.cloud](https://api.alquran.cloud)
- [quran.kemenag.go.id](https://quran.kemenag.go.id)

# REST Endpoints
- `/surah/{surah_number}` : returns surah data including verses.
- `/verse/{surah_number}/{verse_number}` : returns verse data.
- `/topic` : returns list of topics.
- `/topic/{id}` : returns the specific topic id with the verses related to it.

# GQL Endpoints
`/graphql`

example gql surah query:
```{
  surah(surahNumber:2){
    id
    numberOfVerse
    idTranslation
    verses {
      latin
    }
  }
}
```
example verse query:
```
{
  verse(surahNumber:2, verseNumber:2){
    id
    arabic
    latin
  }
}
```
example topics query
```
{

  topics{
    id,
    enTitle,
    idTitle
  }
}
```
example verse topic query
```
{

  verseTopic(topicId:1){
    id,
    enTitle,
    idTitle,
    verses{
      latin
    }
  }
}
```