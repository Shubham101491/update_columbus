<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>ColumbusLost | Home</title>
    <link rel="icon" href="images/favicon.png" type="image/x-icon">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/responsive.css">
    <link rel="stylesheet" href="css/font-awesome.min.css">
    <!-- <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet"> -->
     <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="https://www.jqueryscript.net/demo/jQuery-Plugin-For-Country-Selecter-with-Flags-flagstrap/dist/css/flags.css">
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/flexslider/2.7.0/flexslider.min.css">
     <link href="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/css/select2.min.css" rel="stylesheet" />
     <link href="https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/11.0.9/css/intlTelInput.css" rel="stylesheet" media="screen">
  
</head>

<body class="main">
    <nav class="navbar navbar-default">
        <div class="container">
            <div class="navbar-header"> 
                 <div class="">
                <a onclick="openNav()" class="menu-icon1 dektop-button"><i class="fa fa-bars"></i></a>
                 <!-- <a onclick="openNav3()" class="menu-icon1 mobile-button"><i class="fa fa-bars"></i></a> -->

                
            </div>
            <div class="navbar-logo-image">
                <a href="index.php" class="navbar-brand">
                    <img src="images/icons/logo.png">
                </a>
            </div>
            <div class="search-box">
            <div class="input-group mb-1 ">
            <input type="text" class="form-control" placeholder="">
            <div class="input-group-append">
             <button class="btn btn-search" type="submit"><a href="hotel-search-result.php"><img src="images/icons/search.png"></a></button>
              </div>
            </div>
            <div class="search-cat">
                <ul>
                    <li>
                        <label>Destination</label>
                        <input type="radio" name="search" checked>
                    </li>
                    <li><label>Hotel</label>
                        <input type="radio" name="search">
                    </li>
                    <li><label>Travel</label>
                        <input type="radio" name="search">
                    </li>
                    <li><label>Events</label>
                        <input type="radio" name="search">
                    </li>
                        <li><label>Home Stays</label>
                        <input type="radio" name="search">
                    </li>
                </ul>
            </div>
            </div>
        </div>
            <!-- <div class="" id="myNavbar">
                
            </div> -->
            <div class="navbar-right">
               <div class="country-set">
                        <form>
                            <div class="form-group">
                                <!-- <label>Select Countrys</label><br> -->
                            <div id="basic" data-input-name="country"></div>
                            </div>
                        </form>
                    </div>
                    <div class="nav-2">
                        <a onclick="openNav1()" class="menu-icon1 dektop-button"><i class="fa fa-bars"></i></a>
                        
                    </div>
                    
            </div>
        </div>
    </nav>
<!-----------------left sidebar----------->
    <div id="mySidenav" class="sidenav">
   <ul>
      <li><a href="javascript:void(0)" class="closebtn" onclick="closeNav()">Close &times;</a></li>
      <li><a href="index.php"><i class="fa fa-home"></i>Home</a></li>

      <li><a href="destination-search-result.php"><i class="fa fa-building"></i>Destination</a></li>
      <li><a href="hotel-search-result.php"><i class="fa fa-building"></i>Hotels</a></li>
      <li><a href="homestay-search-result.php"><i class="fa fa-bed"></i>Home Stays</a>
      </li>
      <li><a href="event-search-result.php"><i class="fa fa-calendar"></i>Events</a></li>
      <li><a href="travel-search-result.php"><i class="fa fa-tripadvisor"></i>Tour Operators</a></li>
  </ul>
</div>

<!------------Right Sidebar------------->
<div id="mySidenav1" class="sidenav1">
  
  <ul>
      <li><a href="javascript:void(0)" class="closebtn" onclick="closeNav1()">Close &times;</a></li>
      <li><a href="login-register.php"><i class="fa fa-user"></i>Register/Login</a></li>
      <li><a href="about.php"><i class="fa fa-users"></i>About Columbus Lost</a></li>
      <li><a href="home-advertise-us.php"><i class="fa fa-users"></i>Advertise With Us</a></li>
      <li><a href="contact.php"><i class="fa fa-phone"></i>Contact Us</a></li>
     <!--  <li><a href="#"><i class="fa fa-users"></i>Our Blog</a></li> -->
  </ul>
</div>
<!--------------mobile-view-sidebar-------------->
