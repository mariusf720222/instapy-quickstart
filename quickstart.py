# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'relojesluxuury'
insta_password = '20032003c'

comments = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=relojesluxuury,
                  password=20032003c,
                  headless_browser=False)

with smart_run(session):
  """ Activity flow """		
  # general settings		
  session.set_dont_include(["friend1", "friend2", "friend3"])		
  
  # activity		
  session.like_by_tags(["rolex"], amount=10)

  # Joining Engagement Pods
  session.set_do_comment(enabled=True, percentage=35)
  session.set_comments(comments)
  session.join_pods(topic='watches', engagement_mode='no_comments')
