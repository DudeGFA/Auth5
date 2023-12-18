<!DOCTYPE html>
{% load static %}
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <title>Auth5</title>
  <meta content="" name="description">
  <meta content="" name="keywords">

  <!-- Favicons -->
  <link href="{% static 'images/logo.png' %}" rel="icon">
  <link href="{% static 'images/apple-touch-icon.png' %}" rel="apple-touch-icon">

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="{% static 'bootstrap/css/bootstrap.min.css' %}" rel="stylesheet">

  <!-- Template Main CSS File -->
  <link href="{% static 'css/landing.css' %}" rel="stylesheet">
<body>

  <!-- ======= Header ======= -->
  <header id="header" class="header fixed-top">
    <div class="container-fluid container-xl d-flex align-items-center justify-content-between">

      <a href="index.html" class="logo d-flex align-items-center">
        <img src="{% static 'images/logo.png' %}" alt="">
        <span>Auth5</span>
      </a>

      <nav id="navbar" class="navbar">
        <ul>
          <li><a href="/account/website/login/">Website Account Login</a></li>
          <li><a class="nav-link scrollto" href="/account/login/">User Account Login</a></li>
        </ul>
        <i class="bi bi-list mobile-nav-toggle"></i>
      </nav><!-- .navbar -->

    </div>
  </header><!-- End Header -->

  <!-- ======= Hero Section ======= -->
  <section id="hero" class="hero d-flex align-items-center">

    <div class="container">
      <div class="row">
        <div class="col-lg-6 d-flex flex-column justify-content-center">
          <h1 data-aos="fade-up">Decentralization, Privacy, Data Security and Control</h1>
          <h2 data-aos="fade-up" data-aos-delay="400">We give you total and absolute control of your Personal Identifiable information on the internet</h2>
          <div data-aos="fade-up" data-aos-delay="600">
            <div class="text-center text-lg-start" style="margin-top: 10px;">
                <a href="/account/register"><button class="button-64" role="button"><span class="text">Get started as A web user</span></button></a>
                <a href="/account/website/register"><button class="button-64" role="button" style="margin-top: 10px;"><span class="text">Get started as A website owner</span></button></a>
            </div>
          </div>
        </div>
        <div class="col-lg-6 hero-img" data-aos="zoom-out" data-aos-delay="200">
          <img src="{% static 'images/dec.png' %}" class="img-fluid" alt="">
        </div>
      </div>
    </div>
  </section><!-- End Hero -->
    <div class="container mt-5 mb-5">
      <div class="row align-items-center">
        <div class="col-md-6">
          <img src="{% static 'images/welcome.jpg' %}" alt="Auth5 Logo" class="img-fluid">
        </div>
        <div class="col-md-6">
          <h1 data-aos="fade-up">How Auth5 Works</h1>
          <p class="lead">
            Auth5 is a 3rd party Authentication system but compared to regular Web 2.0 3rd party Authentication, We:
          </p>
          <ol class="lead">
             <li>Don't have or store your personal data</li>
            <li>Ensure None of your Personal Data is shared with websites you authenticate with.</li>
            <li>Ensure your data is only accessed by web users you grant access</li>
          </ol>
          <ul class="lead">
            <li class="lead">You store your data on your Decentralized Web Nodes.</ii>
            <li class="lead">On your Auth5 account you decide the rules and permissions of who can access your data and when they can.</li>
            <li class="lead">We fetch this data from your DWN and send them to web users you grant access to, when these web users visit sites that require your data.</li>
            <li class="lead">This data is sent directly to their browsers. Even web servers of the websites they visit can't access your data.</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="container mt-10 mb-5 text-center">
        <h1 data-aos="fade-up" class="justify-items-center">Secure Data Access with Auth5</h1>
    </div>
    <div class="container mt-5 mb-5">
      <div class="row align-items-flex-start">
        <div class="col-md-6 order-md-2">
          <img src="{% static 'images/data.jpg' %}" alt="Data Access" class="img-fluid">
        </div>
        <div class="col-md-6">
          <p class="lead">
            Safeguarding Personal Identifiable Information (PII) is our priority.
          </p>
          <ul class="lead">
            <li>For pages requiring PII, a request is sent from the user's browser</li>
            <li>The requesting user must be authenticated. We will validate if the data owner has granted the requesting user access.</li>
            <li>If approved, we will fetch the data from the user's secure data vault and forward it to the requesting user</li>
          </ul>
          <p class="lead">Imagine Facebook but:</p>
          <ul>
              <li class="lead">all your personal data is stored with you and not on Facebook Servers</li>
              <li class="lead">Your data isn't sold to advertisers and</li>
              <li class="lead">Only a certain group of people you trust can access any of your personal identifying information on Facebook</li>
          </ul>
          <p class="lead">This is the result on websites you authenticate with Auth5</p>
        </div>
      </div>
    </div>



  <a href="#" class="back-to-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>

  <!-- Vendor JS Files -->
  <script src="{% static 'bootstrap/js/bootstrap.bundle.min.js'%}"></script>

  <!-- Template Main JS File -->
  <script src="{% static 'js/main.js' %}"></script>

</body>

</html>


