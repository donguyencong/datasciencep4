#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 19:02:48 2017

@author: congdonguyen
"""

"""
In the attached file, there are four tables that describe users in a ForEx trading system and their communications via direct messages and forum-style discussion boards.
The file 'users.tsv' contains unique user ids and account creation dates. The file messages.tsv contains unique message ids, send dates, sender ids (consistent with those in 'users.tsv'), and message types.
The file 'discussions.tsv' contains unique discussion ids, creation dates, creator ids (consistent with those in 'users.tsv'), and discussion categories.
The file 'discussion_posts.tsv' contain unique post ids, discussion ids (consistent with those in 'discussions.tsv'), and creator ids (consistent with those in 'users.tsv').

All files are TAB-separated. All times in the tables are expressed in milliseconds, starting on midnight, January 1, 1970. You shall to convert the times to days (24hr).

You shall produce the following deliverables:

Simple descriptive statistics:
How many users are in the database? Deliverable: A number.
What is the time span of the database? Deliverable: The difference between the largest and the smallest timestamps in the database, a number.
How many messages of each type have been sent? Deliverable: A pie chart.
How many discussions of each type have been started? Deliverable: A pie chart.
How many discussion posts have been posted? Deliverable: A number.
Activity range is the time between the first and the last message (in ANY category) sent by the same user. What is the distribution of activity ranges? Deliverable: a histogram
Message activity delay is the time between user account creation and sending the first user message in a specific category. What is the distribution of message activity delays in EACH category? Deliverable: a histogram for each category (ideally all histograms shall be in the same chart, semi-transparent, with legend).
What is the distribution of discussion categories by the number of posts? What is the most popular category? Deliverable: a pie chart, with the most popular category highlighted.
Post activity delay is the time between user account creation and posting the first discussion message. What is the distribution of post activity delays in the most popular category? Deliverable: a histogram. Note: The most popular category shall be carried over from the previous question.


A box plot with whiskers that shows all appropriate statistics for message activity delays in EACH category, post activity delays, and activity ranges.


You shall be able to produce all deliverables in one program by applying appropriate transformations to one DataFrame, assembled from the four tabular files. The Y axis of all histograms shall be on the logarithmic scale.

You shall use Pandas. You shall not use CSV readers or any low-level Python tools to read files. You shall not use any loops or list comprehensions over table rows. (Loops over columns may be allowed, if necessary.)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

discussionPosts = pd.read_table("traders/discussion_posts.tsv")
discussions = pd.read_table("traders/discussions.tsv")
messages = pd.read_table("traders/messages.tsv")
users = pd.read_table("traders/users.tsv")

#Total user
totalUsers = len(users["id"])

#Time stamps
timeData = pd.concat([discussions["createDate"], messages["sendDate"],discussionPosts["createDate"], users["memberSince"] ], ignore_index=True)
timeSpan = (timeData.max() - timeData.min())/(60*60*24*1000)

#Messages type
plt.figure(1, figsize=(10,10))
fraction = messages["type"].unique()
numData = [messages["type"].value_counts()[0], messages["type"].value_counts()[1]]
plt.title("Messages type")
plt.pie(numData, labels=fraction, shadow=True, autopct='%1.1f%%', colors=["red", "orange"])
plt.savefig("images/messagetype.png")
plt.close()

#Discussion category
plt.figure(2, figsize=(10,10))
plt.title("Discussion Category", y=1.1)
discussions["discussionCategory"].value_counts().plot.pie(labeldistance=1.2, shadow=True, autopct='%1.1f%%', pctdistance=1.1, legend=True,explode = (0.2, 0, 0,0,0,0.1,0.1,0.1,0.1))
plt.savefig("images/discusstionCategory.png")
plt.close()

#discussions Posts = 1980
totalDiscussionPosts = len(discussionPosts["discussion_id"].unique())

#Activity range
activityFrame = pd.merge(users, messages, left_on='id', right_on='sender_id')
activityFrame = activityFrame.groupby(["id_x"])
plt.figure(3, figsize=(10,10))
plt.title('Activity Range')
plt.xlabel('Activity Range')
plt.ylabel('Users')
activityData = (activityFrame.sendDate.max() - activityFrame.sendDate.min())/(60*60*24*1000)
activityData.plot.hist(logy=True).set_ylabel("Users")
plt.savefig("images/activityRange.png")
plt.close()

#Message activity delay
plt.figure(4, figsize=(10,10))
plt.title('Message Activity Delay')
activityDelayData = activityFrame.min()
friendRequestData = activityDelayData.loc[activityDelayData['type'] == 'FRIEND_LINK_REQUEST']
friendRequestData = (friendRequestData.sendDate - friendRequestData.memberSince)/(60*60*24*1000)
dMessageData = activityDelayData.loc[activityDelayData['type'] == 'DIRECT_MESSAGE']
dMessageData = (dMessageData.sendDate - dMessageData.memberSince)/(60*60*24*1000)
friendRequestData.plot.hist(legend=True, stacked=True, label='Friend link request', alpha=0.5, logy=True)
dMessageData.plot.hist(legend=True, stacked=True, label='Direct Message', logy=True).set_ylabel("Users")
plt.xlabel("Days")
plt.savefig("images/messageDelay.png")
plt.close()

# Discussion posts
plt.figure(5, figsize=(10,10))
plt.title('Discussion Posts')
discussionDistributionFrame = pd.merge(discussionPosts, discussions, left_on='discussion_id', right_on='id')
discusstionDistributionData = discussionDistributionFrame.discussionCategory.value_counts()
discusstionDistributionData.plot.pie(legend=True, labeldistance=1.2, shadow=True, autopct='%1.1f%%', pctdistance=1.1, explode = (0.2, 0, 0,0,0,0.1,-0.2,0.3,0)).set_ylabel("")
plt.savefig("images/posts.png")
plt.close()

#Post activity delay
plt.figure(6, figsize=(10,10))
postActivityDelayFrame = pd.merge(discussionPosts, users, left_on='creator_id', right_on='id')
postActivityDelayData = postActivityDelayFrame.groupby("creator_id").min()
postActivityDelayData = (postActivityDelayData.createDate - postActivityDelayData.memberSince)/(60*60*24*1000)
plt.ylabel('Users')
plt.xlabel('Days')
postActivityDelayData.plot.hist(logy=True, title="Post Activity Delay").set_ylabel("Users")
plt.savefig("images/postsDelay.png")
plt.close()


#A box plot with whiskers that shows all appropriate statistics for message activity delays in EACH category, post activity delays, and activity ranges.
plt.figure(7, figsize=(10,10))
plt.subplot(1, 4, 1)
plt.title("Friend Request")
friendRequestData.plot.box(label="", showmeans=True).set_ylabel("Box plot")
plt.yscale('log')
plt.subplot(1, 4, 2)
plt.title("Direct message")
dMessageData.plot.box(label="", showmeans=True)
plt.yscale('log')
plt.subplot(1, 4, 3)
plt.title("Post Activity")
postActivityDelayData.plot.box(label="", showmeans=True)
plt.yscale('log')
plt.subplot(1, 4, 4)
plt.title("Activity")
activityData.plot.box(label="", showmeans=True)
plt.yscale('log')
plt.tight_layout()
plt.savefig("images/boxPlot.png")
plt.close()
