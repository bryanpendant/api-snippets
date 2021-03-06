<?php
// Get the PHP helper library from twilio.com/docs/php/install
require_once('/path/to/twilio-php/Services/Twilio.php'); // Loads the library

// Your Account Sid and Auth Token from twilio.com/user/account
$sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"; 
$token = "your_auth_token"; 
$client = new Services_Twilio($sid, $token);

// Get an object from its sid. If you do not have a sid,
// check out the list resource examples on this page
$participant = $client->account->conferences->get('CFbbe4632a3c49700934481addd5ce1659')->participants->get("CA386025c9bf5d6052a1d1ea42b4d16662");
echo $participant->start_conference_on_enter;
