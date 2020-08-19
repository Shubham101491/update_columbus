<!DOCTYPE html>
<html>
<head>
  <title>ColumbusLost|Dashboard</title>
  <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="icon" href="images/favicon.png" type="image/x-icon">
   <!--  <link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"> -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
     <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.20/css/dataTables.bootstrap4.min.css">

    <link rel="stylesheet" type="text/css" href="css/dashboard.css">
    <link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-multiselect/0.9.13/css/bootstrap-multiselect.css">
     <link href="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/css/select2.min.css" rel="stylesheet" />
     <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
     <link href="https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/11.0.9/css/intlTelInput.css" rel="stylesheet" media="screen">
</head>

<div id="wrapper">

  <aside id="sidebar-wrapper" class="shadow1">
    <div class="sidebar-brand">
      <a href="dashboard.php">
      <img src="images/icons/logo-color.png" class="desktop-logo"></a>
    </div>
    <ul class="sidebar-nav">
      <li class="active">
        <a href="dashboard.php"><i class="fa fa-dashboard"></i>Dashboard</a>
      </li>
      <li>
        <a href="profile.php"><i class="fa fa-user"></i>My Profile</a>
      </li>
      <li>
        <a href="post-hotel.php"><i class="fa fa-building"></i>Post a Hotel</a>
      </li>
      <li>
        <a href="my-hotel.php"><i class="fa fa-building"></i>My Hotel</a>
      </li>
      <li>
        <a href="post-homestay.php"><i class="fa fa-bed"></i>Post a Homestay</a>
      </li>
      <li>
        <a href="my-homestay.php"><i class="fa fa-bed"></i>My Homestay</a>
      </li>
       <li>
        <a href="post-event.php"><i class="fa fa-calendar"></i>Post an Event</a>
      </li>
      <li>
        <a href="my-event.php"><i class="fa fa-calendar "></i>My Event</a>
      </li>
       <li>
        <a href="list-business.php"><i class="fa fa-address-card"></i>List Your Business</a>
      </li>
      <li>
        <a href="my-business.php"><i class="fa fa-address-card"></i>My Business</a>
      </li>
       <li>
        <a href="advertise-us.php"><i class="fa fa-adn"></i>Advertise With Us</a>
      </li>
       <li>
        <a href="premium-listing.php"><i class="fa fa-adn"></i>My Premium Listing</a>
      </li>
    </ul>
  </aside>

  <div id="navbar-wrapper">
    <nav class="navbar navbar-inverse">
      <div class="container-fluid">
        <div class="header-cont d-flex justify-content-between">
        <div class="navbar-header">
          <a href="#" class="navbar-brand" id="sidebar-toggle"><i class="fa fa-bars"></i>
           <img src="images/icons/logo.png" class="mobile-logo"></a>
          <!-- <a href="dashboard.php  ">
     </a> -->
        </div>
        <div class="head-right">
          <ul>
            <li>
          <div class="dropdown">
    <button type="button" class="btn btn-notification dropdown-toggle notification" data-toggle="dropdown"><i class="fa fa-bell"></i>
    </button>
    <div class="dropdown-menu">
       <ul  id="web-notification" class="notification-lsit">
                                     <li id="nid_829"> 
                  <a href="#">
                  
                                       <img src="images/icons/family.png" class="notification-user">
                                          <div class="mobiledatabox">
                     <div class="mobbox web-box">
                     
                     <h2>jitendra</h2>
                        <h4>Just Now</h4>
                                </div>
                                
                     <div class="mobbox">
                   
                    <span style=" color: #3CAE24;">Somebody book post a Event</span>
                    </div>
                    </div>
                    </a>
                    </li>
                                      <li id="nid_828"> 
                  <a href="#">
                  
                                       <img src="images/u.png" class="notification-user">
                                          <div class="mobiledatabox">
                     <div class="mobbox web-box">
                     
                     <h2>jitendra</h2>
                        <h4>Just Now</h4>
                                </div>
                                
                     <div class="mobbox">
                   
                    <span style=" color: #3CAE24;">Somebody book a Hotel</span>
                    </div>
                    </div>
                    </a>
                    </li>
                                      <li id="nid_827"> 
                  <a href="#">
                  
                                       <img src="images/u.png" class="notification-user">
                                          <div class="mobiledatabox">
                     <div class="mobbox web-box">
                     
                     <h2>jitendra</h2>
                        <h4>Just Now</h4>
                                </div>
                                
                     <div class="mobbox">
                   
                    <span style=" color: #3CAE24;">Somebody post a Homestay</span>
                    </div>
                    </div>
                    </a>
                    </li>
                                      <li id="nid_826" > 
                  <a href="#">
                  
                                       <img src="images/u.png" class="notification-user">
                                          <div class="mobiledatabox">
                     <div class="mobbox web-box">
                     
                     <h2>jitendra</h2>
                        <h4>Just Now</h4>
                                </div>
                                
                     <div class="mobbox">
                   
                    <span style=" color: #3CAE24;">Somebody book a hotel</span>
                    </div>
                    </div>
                    </a>
                    </li>
                  </ul>
    </div>
    <span class="badge">3</span>
  </div>

</li>
<li><a href="index.php"><i class="fa fa-power-off"></i></a></li>
</ul>
</div>
      </div>
    </div>
    </nav>
  </div>
