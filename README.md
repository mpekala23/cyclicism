# [Cyclicism](https://cyclicism.mark-pekala.dev)

Sure, the news is sensational... _but don't you feel like you're read it before?_ This project aims to show you that you have, or at least that you've read something semantically very similar.

My goal is to make people think more critically about the news they consume. I'm hoping that by highlighting patterns in "top" stories and the way they're told I can give people tools to separate signal from noise.

Plus, I'm hoping to make the news fun to read again (for myself).

## How does it work?

It's pretty straightforward.

1. I scraped 5 years of data from [The New York Times](https://developer.nytimes.com/apis).
2. I applied an [out-of-the-box sentence transformer](https://www.sbert.net/#) to turn the headline, abstract, and lead paragraph of each article into vectors.
3. I took advantage of [annoy indexes](https://github.com/spotify/annoy) to create simple approximate-nearest-neighbor indexes on this data which could be saved to a file and loaded into memory when needed.
4. I wrote a script which would fetch the latest headlines on The New York Times and find the closest thing indexed and set it to run every 6 hours.
