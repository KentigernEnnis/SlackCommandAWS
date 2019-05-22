# SlackCommandAWS
Simple example of how to get a slack slash command to integrate with AWS API Gateway

I struggled a lot with getting all the pieces wired together so I figured I'd create an example project to show some of the Gotchas in this otherwise pretty straightforward process. 
For this, you'll need access to a Slack workspace and an app within it, as well as an AWS account.  Costs can vary but I believe these are in the free tier (if not, they're extremely inexpensive, especially compared to just about anything else out there).

The simple example I'm going to demonstrate is the ability to throw a ping pong ball at another user.

The way this will work:
- User executes `/ping username`
- Slack sends command to the API Gateway
- API Gateway routes to Lambda
- Lambda returns result that's shown in Slack (Note, if the process takes more than a few seconds, there's a url to call back)

Steps to be completed:

- Create a Lambda
-- From Scratch, give it a name you'll remember.  I've provided an example in Python 3.  I'd recommend a new role, too.
-- Copy in the provided code and Save
- Create a REST API in API Gateway
-- The defaults work well enough for the basic settings.  Give it a fun name.
-- Add a Resource from the Actions menu (Enable CORS to save headaches later)
-- With that resource selected, click Actions and add a Method.  Select Post and hit the checkmark.
-- Select Lambda and select Region your Lambda is in, then select your Lambda function and Save. (Accept the security prompt)
-- Select the Integration Request and expand Mapping Templates.
-- Click "Add mapping template" and enter `application/x-www-form-urlencoded` into the box.
-- Paste the contents of the encoding file into the text box (which usually renders such that you have to scroll down).
-- Save
-- Select Actions menu again and select Deploy -> new Stage.  Give a name for the stage (I use v1 but I've never actually moved to v2).  Hit Deploy
-- Copy Invoke URL that is shown.
- Create Slack App
-- In the Slack app directory, select Build on the top, then Your Apps, then Create New App and provide a cute name and your workspace.
-- Select Slash Commands, Create New Command and call it `/ping` to match my example, pasting in the URL from the API Gateway next (don't forget to include your resource, too), then a short description and hint.  You can play with the escaped things later, we're keeping it super simple now.
-- Go to OAuth & Permissions and click "Install App to Workspace" and Authorize.

That should be it, now you can go test it in your slack workspace.  Troubleshooting is done via the Lambda -> monitoring -> view logs in cloudwatch.
