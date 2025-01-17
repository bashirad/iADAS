<!DOCTYPE html>
<html lang="en">
<head>
    <meta chartset="utf-8">
    <title>Rhinebeck: Asher Dam Alert System</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="/stylesheets/style.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
</head>
<body>
<!--Server Message Modal-->
<div id="serverMessageModal">
    <div id='message'></div>
</div>

<!--Header-->
<div id="header">
    <a href="https://www.rhinebecknyvillage.org/" target="_blank"><img id="seal" src="/images/seal.png"></a>
    <div id="websiteTitleDiv">
        <p id="title">A<span class="small-title-text">sher</span> D<span class="small-title-text">am</span> A<span class="small-title-text">lert</span>
            S<span class="small-title-text">ystem</span></p>
        <p id="subtitle">Flood Prevention Calculator</p>
    </div>
    <img id="logo" src="/images/logo.png">
</div>

<!-- this is not currently functional. A placeholder until we can get a user/pass database-->
<div id="adminLoginContent">
    <div id="adminLoginFormDiv">
        <div id="adminLoginFormCard">
            <form id="adminLoginForm" action="/admin.html">
                <label for="text">Username:</label><br>
                <input type="text" id="username" name="username" value=""><br>
                <label for="password">Password:</label><br>
                <input type="text" id="password" name="password" value=""><br>
                <input type="submit" value="Submit">
            </form>
        </div>
    </div>
</div>
<script src="/javascript/modal.js"></script>
<script src="/javascript/utils.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</html>