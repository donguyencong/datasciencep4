# datasciencep4
Pandas project
In the attached file, there are four tables that describe users in a ForEx trading system and their communications via direct messages and forum-style discussion boards. The file 'users.tsv' contains unique user ids and account creation dates. The file messages.tsv contains unique message ids, send dates, sender ids (consistent with those in 'users.tsv'), and message types. The file 'discussions.tsv' contains unique discussion ids, creation dates, creator ids (consistent with those in 'users.tsv'), and discussion categories. The file 'discussion_posts.tsv' contain unique post ids, discussion ids (consistent with those in 'discussions.tsv'), and creator ids (consistent with those in 'users.tsv').

All files are TAB-separated. All times in the tables are expressed in milliseconds, starting on midnight, January 1, 1970. You shall to convert the times to days (24hr).

You shall produce the following deliverables:

Simple descriptive statistics:
How many users are in the database? Deliverable: A number. 
What is the time span of the database? Deliverable: The difference between the largest and the smallest timestamps in the database, a number. 
How many messages of each type have been sent? Deliverable: A pie chart. 
How many discussions of each type have been started? Deliverable: A pie chart. 
How many discussion posts have been posted? Deliverable: A number.
Activity range is the time between the first and the last message (in ANY category) sent by the same user. What is the distribution of activity ranges? Deliverable: a histogram. 
Message activity delay is the time between user account creation and sending the first user message in a specific category. What is the distribution of message activity delays in EACH category? Deliverable: a histogram for each category (ideally all histograms shall be in the same chart, semi-transparent, with legend).
What is the distribution of discussion categories by the number of posts? What is the most popular category? Deliverable: a pie chart, with the most popular category highlighted.
Post activity delay is the time between user account creation and posting the first discussion message. What is the distribution of post activity delays in the most popular category? Deliverable: a histogram. Note: The most popular category shall be carried over from the previous question.
A box plot with whiskers that shows all appropriate statistics for message activity delays in EACH category, post activity delays, and activity ranges.
