#Schlayballs Master Phishing Education Class used by some pro cyber con Artist


Ahoy, cyberhomos!! Ready to cast a net and hook your mocked friends? "Reel 'Em In" is a mock phishing study and a practical skill for managing both front end and back end servers. 
Built with Flask, SQLite, and ngrok, this project spins up a suspicious webpage to lure unsuspecting clickers. Every click gets logged with the front end's biting your bait and getting hooked, compiling all their responses in real-time you can see in your SQLite. My victims(friends) typed "6969" or "420" and sometimes "Banned!" for the fish nibbling the bait. With email alerts that alert victims gently and a debrief that schools them on phishing scams, this is cybersecurity education with some serious MOCKS!

Click Trolling: SQLite logs every click with the precision of a fish counter at a sushi bar. First click? "6969" for the win. Back for more? "Banned!" with a digital dunce cap. Timestamps and anonymized IPs keep it legit.

Sassy Emails: Caught a fish? The system fires off an email like, "Congrats, you fell for a fake fish! Time to scale up your scam-spotting skills!" using secure email magic.

Ngrok Shenanigans: Ngrok turns your localhost into a public URL faster than you can say "phishing pole." Share the link and watch your friends flounder from anywhere!

Edutainment Debrief: After the prank, users land on a page that spills the tea: "You got fished! Here’s how to spot real scams without crying into your tackle box."

Tech Stack  
Flask: The Python web framework that serves up scam pages smoother than a conman’s sales pitch.

SQLite: A lightweight database for storing click logs, because even fake fish deserve a permanent record.

Ngrok: Tunnels your local server to the web, making it easier to cast your net far and wide.

SMTPlib (or pals): Powers those snarky email taunts to your freshly hooked victims.

HTML/CSS: For a phishing page so tacky it could star in a 90s Geocities reunion tour.

How It Works  
Rig the Trap: Fire up the Flask app and let ngrok give you a public URL. Set up SQLite to log your catches and secure your email credentials (no real fish were harmed).

Cast the Line: Send the ngrok link to your consenting buddies, disguised as a deal too fishy to resist—like "Free Trout Jacuzzi Vacation!" or "Adopt a Pet Carp Today!"

Hook, Line, Sinker: When a pal clicks the shiny button, SQLite logs it with a timestamp and a zinger: "6969" for a fresh catch, "Banned!" for greedy fish who keep biting.

Reel ’Em In: An email hits their inbox, cackling, "You swam right into our net! Study up on phishing or you’ll be sleeping with the fishes!"

Teach the Fish: Redirect them to a debrief page with a wink: "You’re not a shark yet—here’s how to swim past real scams."

Ethical Fine Print  
Consent or Bust: Only prank friends who’ve signed up for your cyber-fishing trip. No poaching strangers!

Spill the Beans: Reveal the joke post-click with a big, friendly "It’s just a prank, bro!"

Keep It Clean: Anonymize IPs, secure email creds, and delete data after the laughs. No one wants a lawsuit with their trout.

Humor, Not Humiliation: Keep the roasts kinder than a campfire fish fry—education’s the goal, not tears.

Sample Log Output  
plaintext

[2025-04-26 12:34:56] Chad took the bait! Log: 6969
[2025-04-26 12:35:02] Chad’s back for seconds! Log: Banned!




## Setup
1. Clone: `git clone https://github.com/schlayguy/prank-webpage`
2. Install: `pip install -r requirements.txt`
3. Run: `python server.py`
4. ngrok: `ngrok http 5000` (use ARM64 binary for aarch64)
5. Email: Update `send_email.py`.

## Features
- Logs to `responses.txt`, `responses.db`.
- Sends mock phishing emails.
- Live at: https://a480-2600-1700-17f0-5eb0-216-3eff-fef1-4316.ngrok-free.app/

## Fiverr
Hire me: [fiverr.com/schlayguy](https://fiverr.com/schlayballs)
