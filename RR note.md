
**local notice:**
UI: http://localhost:4200/
api: 
- only one /api/
- use 8080 
- url http://localhost:8080/api/testScheduler?frequency=weekly&isDryRun=true
apikey: check application.properties 

**other env**:
api: 
- two /api/
- dont use 8080 as url
- url https://dev.regulatoryregistry.gov.on.ca/api/api/testScheduler?frequency=weekly&isDryRun=true

**bitbucket:**
Username: andy.liu2@ontario.ca
Temp Password: Friday2025$

**RR public secure:**
Username: andy.liu2@ontario.ca
Temp Password: L1uConG0813!

andydiii0813@gmail.com
L1uConG0813!

c644liu@uwaterloo.ca
l1uConG0813!

**Legacy RR backoffice UAT:**
https://intra.stage.sus.gov.on.ca/registryadmin/bo_login.jsp

Admin:
User ID: chenji
Password: ORRM_test123

Editor:
User ID: chen1ji
Password: ORRM_test123!

user:
liuco
ORRM_test123!

**back end:**
- PostingController is for the api of posting
- PostingDTO is the data from DB after converting the type e.g. Date-> format tobe 'd mm y'
- Posting is the raw data from DB without any converting the type

controller(request) 
-> service 
-> repository 
-> entity <-> DB

**email alert trigger in postman:**
URL: https://dev.regulatoryregistry.gov.on.ca/api/api/testScheduler?frequency=daily&isDryRun=true

replace the domain to the current domain

misccontroller testscheduler params in postman

in postman specify post method, params will be auto changed once url is put in, header need to add X-API-KEY, value depends on differnt env, we can find it in search application will give something like `application.dev.property`. (application.property is local env file)

url: https://dev.regulatoryregistry.gov.on.ca/api/api/testScheduler?frequency=daily&isDryRun=true

isdryrun set to true means wont trigger real eamail sent rn, but false will trigger it to be sent right now.

this test is based on today morning's expected email alert to be received.

weekly:
postings that updated *last 7 days* suppose today is tuesday, if there is update from last tuesday to this monday then we get alert. different than normal we receive weekly on monday for the updates between last monday to sunday.


## RR testing sender email
orrm.test@gmail.com
ORRM_test!2025

orrm.test2@gmail.com
ORRM_test!2025 

## git pull
git pull origin main - merge from remote main into local andy-dev, but this uses default merge(cause the original commit messages combined into one merge commit message), not fast-forward merge( will have same commit messages as original ones).

what people do:
1. pull remote dev into local dev first.
2. **fast-forward** merge local dev into local andy-dev. (local andy-dev will show exactly same commits as locla-dev & remote-dev)
3. commit and push local new changes to remote andy-dev. (this will take commits from remote dev(as we merged local-dev into local-andy) and new changes made myself onto remote andy-dev). 

controller 对应api url，比如api/positng/specification 就在controller posting controller.

https://localhost:8080/api is the request for backend 
https://localhost:4200 is for frontend


domain(after the https://) <-> Ip address followed by an port number like 8080, 4200...
localhost <-> 127.0.1 is the local IP address 
localhost is a variable for IP address


## eSMT
incident are the defects found in PROD.
CR wont issue a ticket but just in SP.


## self testing local for 280
1. update profile, everything except title unchanged - DONE
2. update profile, subtitle wrong when user is organization user - Fixed
3. update profile, leave title blank, everthing else fileld out, error expected - DONE 
4. create a new organization user profile  - DONE
5. create a new organization guest profile - DONE

defect 300 workflow
user click follow button -> UserManagementController.java: createUserFollowedPosting -> userFollowedPostingService  Create -> userFollowedPostingRepository -> this followed posting is added into userfollowedposting table -> emailAlertScheduler (when to send, what to send is done here) ->  email sender  

CR 293:
new filter in search page e.g. anticipated effective date


## This application uses Microsoft Azure AD (Active Directory) SSO with the Microsoft Authentication Library (MSAL):

1. clarifications about Microsoft Azure AD:
- its a identity provider
- stores and manages users, groups, roles, permissions.
- It’s the place your application "trusts" to authenticate users (verify who they are) and optionally authorize them (decide what they can access).
In this project:
- Azure AD is where the regulatory registry application "redirects" users to log in.
- Users don’t log in directly to your app with local credentials; instead, they authenticate through Azure AD.
- After successful login, Azure AD issues a token (like an ID token or access token) that your app can use to identify the user and, if needed, call APIs securely.

2. Microsoft Authentication Library (MSAL)
- Now, MSAL is the client-side helper library your app uses to talk to Azure AD.
- It handles the complicated parts of authentication for you.
  - Instead of you manually redirecting, parsing tokens, and refreshing them, MSAL does that.
- On the front-end (React), MSAL is used to trigger sign-in, sign-out, and acquire tokens. E.g., when a user clicks "Login", MSAL redirects them to Azure AD’s login page. Once the user authenticates, MSAL parses the returned JWT tokens (ID token, access token).


**SSO Implementation Overview**
We implemented Azure AD SSO using MSAL, which provides:
- **Seamless** user experience through (**automatic** login and **silent** token refresh)
- Enterprise **security** via Azure AD integration and group-based roles

benefits: 
User Experience: No repeated logins across applications
Security: Centralized authentication through Azure AD

1. "How does your app handle authentication?"
"We use Azure AD SSO with MSAL for seamless enterprise authentication"
1. "What happens when a user's session expires?"
"MSAL automatically refreshes tokens silently, maintaining the SSO experience"
1. "How do you implement role-based access?"
"We map Azure AD groups to application roles using Microsoft Graph API"
1. "What security measures are in place?"
"No hardcoded secrets, environment-based configs, and secure token storage"
1. "How scalable is your authentication solution?"
"Azure AD can handle thousands of users and easily integrate with more applications"


