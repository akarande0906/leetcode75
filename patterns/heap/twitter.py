'''
Leetcode 355: Design Twitter
'''
from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.count = 0 # keeping track of tweets in chronological order
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set) # Set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Update the tweet_map
        # Get the current count and add one to it
        self.tweet_map[userId].append([self.count, tweetId])
        self.count += 1 # To maintain order 

    def getNewsFeed(self, userId: int) -> List[int]:
        # Build the news feed 
        news_feed = []
        max_heap = []
        self.follow_map[userId].add(userId)
        for user in self.follow_map[userId]:
            # Start in reverse as the most recent tweet is added later
            for count, tweet in self.tweet_map[user][::-1]: 
                heapq.heappush(max_heap, [count, tweet])
                if  len(max_heap) > 10: 
                    # Remove the oldest tweet
                    heapq.heappop(max_heap) 
        for _ in range(len(max_heap)):
            count, tweet = heapq.heappop(max_heap)
            news_feed.append(tweet)
        return news_feed[::-1] # Newest tweets first

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
twitter = Twitter()
twitter.postTweet(1,5)
print(twitter.getNewsFeed(1))
twitter.follow(1,2)
twitter.postTweet(2,6)
print(twitter.getNewsFeed(1))
twitter.unfollow(1,2)
print(twitter.getNewsFeed(1))

# Time Complexity: O(kLogk) for the news feed where k is the total number of tweets for that user's followees
# It takes log(k) to sort a heap, for k tweets. We reverse the result array but that is O(10) at max which is constant
# For the other functions its O(1)
# Space Complexity: The Max Heap will have at most 10 elements. We will need O(nk) space for the tweet map where n is th number of users
# The follower map will have O(n^2) assuming all users follow all other users


