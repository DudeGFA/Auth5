# Auth5
MAVIGO DevCareer Web5 hackathon repo

Auth5 is a web5 3rd party Authentication system.
Auth5 helps users sign into and use web applications without sharing any of their personal information with such applications.
It also ensures users have full control of and can determine who can view / access their data on a website.

Auth5 users will have to create an account on Auth5. A user Id and authentication token is automatically generated..
On the Auth5 dashboard, User’s will specify the corresponding records of their PII and their DIDs.

Websites will also have to create an account on Auth5. Each website will be associated with an ID.

When a user tries to log into a web application, there will be a sign-in with the Auth5 button.
When clicked, a dialog box / page pops up and the user enters his Auth5 username and password.

If these details are correct:
	If the user has no previous account on the website, an identification string is generated on Auth5 servers and sent to the website the user is trying to authenticate with. The website saves this string and uses it to identify the user. Auth5 also stores this string and uses it to link the user to his account on the site.

	If the user already has an account on the site, his/her Id is fetched and sent to the site with an authentication and the user is logged in.

None of the user’s personal identifiable information is stored on the site but instead stored on DWNs.

Only users who a data owner grants access can view any of his/her personal identifiable information.

Let’s say user A visit’s user B’s profile. A script running on the user’s browser will send a request to Auth5 with the following details:
- Website’s ID
- User A ID
- User B ID
- A list of fields required to view user B’s profile

Auth5 checks if User A granted permission to User B’s to access the data he is requesting. If he did, the requested data is gotten from user B’s DWN and returned to the web browser else, the data won’t be returned and the page won’t be viewable or the user B’s PII won’t be available on the page.

There will be later improvements to set protocols and define rules on what data can be accessed by whom e.g only people from Africa that are between 30 - 40 years old can view my data of birth e.t.c. Websites could also request certain required data from users such as hair colour, height e.t.c but we might now work on this now. Let’s get the MVP up and running.
## Authors :
* Twitter: **[God'sfavour Idowu-Agida](https://twitter.com/DudeGFA)** Github: <[DudeGFA](https://github.com/DudeGFA)>
* **Mahlet Seifu** Github: <[Mahlet2123](https://github.com/Mahlet2123)>
