# Appslify Music Service

## Objective
Create a service called "Appslify" that simulates playing music.

## Functional Requirements

## Stage 1
Play & Shuffle: The service must "play" each song in the list by printing its title
to the console. When the playlist ends, shuffle it (i.e., randomize the order of the songs) and continue playing.

```python
playlist = ["Gods Plan", "A LA SALA", "Hate That I Love You", "Texas Sun", "Gods Plan"]
```

### API
Classes:
- MusicPlayer(playlist)  
Functions:
- play(): shuffle & play the playlist endlessly.

### Stage 2
Unique Play: Ensure no song is played twice consecutively — even if it appears more than once in the same playlist.

### Stage 3
Playlist Selection: Your service should select the playlist that is closest to the current date.

```python
playlists = {
"20240131": ["Gods Plan", "A LA SALA", "Hate That I Love You", "Texas Sun", "Gods Plan"],
"20240130": ["Another Love", "THANK GOD", "THANK GOD", "Gods Plan", "fukumean"],
"20240115": ["Tobacco Sunburst", "Tobacco Sunburst", "Sofia", "Bloom Later", "Gods Plan"],
"20230201": ["Gods Plan", "Nonstop", "In My Feelings", "In My Feelings", "March 14"]
}
```

### API
Classes:
- MusicPlayer(playlists)  
Functions:
- get_closest_playlist(): get the closest (by date) playlist.

### Stage 4
Data Fetching: 
Your service must fetch songs from a provided endpoint:
[`https://run.mocky.io/v3/741ebf09-a77a-4c0d-9951-9fab50dd6ccf`](https://run.mocky.io/v3/741ebf09-a77a-4c0d-9951-9fab50dd6ccf)  

### API
Classes:
- MusicPlayer(url)  
Functions:
- fetch_playlists(): get the playlists from the endpoint.


## Non Functional Requirements

- Output: 
  - Console logs of the song titles as they are "played" 
  - A final count of how many times the entire playlist was played after service interruption.

## Evaluation Criteria
Submissions will be evaluated based on programming best practices and solution correctness.

## Questions
If you have any clarifications or issues, please share with us.