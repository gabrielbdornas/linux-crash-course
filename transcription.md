hey I'm Dave and this is a linux video
course I started making this for a
friend but I figured other people could
benefit and if I'm going to take the
time to really cover Linux from sort of
the basics all the way to a intermediate
/ advanced administrator level I just
figured it's something that other people
could benefit from why Linux
well Linux is cool it's got a huge
community it's sort of cutting edge an
unbelievable amount of stuff runs on
Linux
so if you like in terms of percentage of
the world's websites or mail servers or
just all these services run on Linux and
more and more also client systems so
end-user systems that is even business
people and stuff are using computers
that are running Linux it's great work
it's awesome to learn it's fun to do it
also happens to be a great career and
really well paid you can do it basically
regardless of your formal qualifications
that is you don't need to study to
become a system administrator or start
your career in less you don't need a
degree generally people are really just
looking for skill knowledge about the
systems and some experience in using the
tools that are used in production so the
programs and stuff in Linux so this is a
great thing to do if you're just looking
for a cool thing to learn or a career
change or to understand more about
computers and security it allows you to
do cool stuff even if you're not
interested in a career in Linux like
just running a bunch of services at home
it's a lot of fun to have like a torrent
server that's always downloading the
torrents legal torrents of course
because you would never do anything
illegal or things like setting up a
streaming movie server for your friends
or your family at your house doesn't
matter if they're running Linux I mean
they don't have to know that the server
is running Linux so they could stream
movies or TV shows from anywhere in the
house
you could set up a mail server to
protect your privacy or the privacy of
your family you could run websites or
forums or a blog from your house you
could set up a programming environment
or even learn stuff like security or you
know quote unquote hacking which is a
misnomer but we'll get into that later
so basically how this course works it
requires a small commitment from you and
that is to really get the full value out
of this course you have to commit to it
just let's say for 30 days if you watch
these videos every day and you watch it
in the order that I create the videos in
you try everything at home just watching
these isn't gonna be enough to give you
a solid understanding your fingers have
to type these things that I'm typing and
you have to play around with them even
once the video ends so experiment at
home and don't be afraid to break stuff
we're going to use a virtual machine to
run Linux in so you have a little play
environment even if you've got Mac OS X
or Windows you can run some Linux just
like any other application and
experiment around and if you blow it
away then it's okay you can just start
from scratch without hurting the rest of
your system so it's race it's become
very safe God knows when I was learning
this stuff I blew away my parents
machine so many times and I think I lost
their data once I mean just everything
was gone and you don't need to run that
risk anymore computers are so powerful
now that you can run operating systems
inside of other operating systems so
what's covered in this course
specifically if you go through this
course my commitment is to help you
understand how Linux works not just on
the surface you know Linnet running
Linux at home has become incredibly easy
over the last 10 years you know you
never have to look at a command-line
utility if you just want to run Linux at
home and it's great for that like it's
what I would install on my grandmother's
computer because you know it's going to
be the most secure and simple to use
thing by default for people who just use
things like email and Facebook and and
you know I browse the web which is
almost everyone these days
but this isn't that this is not a guide
to running like a Linux desktop at home
this is a deep dive into the Linux
system itself it's really going to help
you understand the operating system and
that will allow you to do all kinds of
things that are way way cooler than just
running a desktop system at home this
course is gonna be command-line heavy
about I want to say everything but you
know I I know I'm gonna break that
promise at some point but like 99% of
what I'm gonna show you is done in the
shell so in this environment that you're
seeing here we're gonna help you become
a command-line ways right now I'm gonna
be focusing on the most common shell
commonly found in the most popular Linux
distributions and that's bash the
born-again shell we're going to talk
about the boot process and system in it
so the startup of a Linux kernel and
userland stuff we're gonna talk about
access control and root or God powers
we're gonna talk about how the
filesystem is laid out where everything
is how it works
we're gonna talk about process control
so controlling the processes or
applications as they run and then we're
gonna get as quickly as possible into
you comments this admin tasks so
managing users managing storage managing
packages and security patches updating
software we're gonna cover the most
common remote tools for a remote system
administration it's like SSH secure
shell which is a cryptographically
secure shell you can connect from one
computer to the other and work on it as
if it were local and things like backup
that use those tools we're gonna cover
sort of basic problem solving and
troubleshooting methodology and other
things like just you know where the log
files are and sort of good to know stuff
like that application configuration of
course is part of this common services
that you would want to run or would be
running in a production system so in a
professional setting like that or even
at home really I mean file sharing web
like these
all things you can run from home but
we'll also talk to security in a way
that's a little bit more professional
than perhaps you would need at home but
it's obviously still useful for home use
we'll talk about the Linux kernel itself
now Linux really is just the kernel
which is the very core of the operating
system in the operating system itself
but most of the software you're going to
use on Linux it's new software so it's
actually the real term and there's like
huge philosophical battles over this but
it's new Linux not just Linux look a new
people get very angry when you call it
just Linux so it's a little kernel and a
good new user land system but we're
talking about the kernel so Linux itself
underneath all there we're gonna
basically peek up the skirt of this
whole machine and see how it all works
and that's that's starting to get into
real that's in the weeds basically
that's pretty pretty heavy technical
stuff then but you'll be able to
understand it by the time we get to it
and that's also when we'll cover
networking basics so tcp/ip networking
which is the way the internet works
basically and the layers of that and how
they interact and it will even cover
some advanced networking and security so
also some of the networking applications
that run like how routing works on the
internet how DNS the domain name system
works and some some security knowledge
I'll also cover and then we'll even get
into some more advanced networking and
security concepts like routing how
routing works on the internet DNS or the
domain name system intrusion detection
vulnerability scanning checking your
machines to see if you can get into them
seeing if they're vulnerable to things
and then some resources for going
further down that road we're not going
to go down like the hacking pentesting
road too far but this certainly will
give you the foundation you absolutely
need if you ever want to do that because
you're absolutely no good to anyone as
like a hacker for hire that is you know
sort of a penetration tester if you
don't know like the fundamentals of
tcp/ip networking and that's what I'll
give you here
also just for those of you who are
interested in getting work as Linux or
UNIX system administrators it's a
phenomenal career it is my chosen career
I'll give you some words on like job
hunting certifications that might be
useful additional skills that you might
need that kind of thing so if you really
stick with this and you commit to going
through this course you're gonna learn a
lot about Linux that is my commitment to
you good but basically your grandma
can't sit down and take this course
here's the deal if you're already
reasonably proficient on a computer so
like you know what a CPU is and you know
that that's a processor and you know the
difference between memory or RAM and
hard drive space and you know what a
command line or shell is or have at
least heard of these things then you can
you can take this course if you don't
know these things if you have really if
you're sort of a computer newbie this
course is not for you you need to get
some basic knowledge first and then you
can do this this is sort of starting to
be intermediate to advanced computer
years now I'll cover the basics I will
cover very basic shell commands like
moving around the file system on the
shell so even if you've never worked on
the shell before or very little or
you've only copy and pasted things in
there to try to get things working
that's fine we'll cover what you need to
know but I'm not going to cover it in
huge detail so the less you know the
more kind of work you'll have to do to
get caught up to where we start so I
hope that gives you a good idea where
we're going and what this course can do
for you yeah let's get started just
general outline most video I'm gonna try
to keep the videos as short as possible
this will hopefully be a fairly long
video in terms of the basic set of
videos but then as we get to more
advanced topics they'll obviously
require more time to cover so you know
we'll get back into the 15 minute to 20
minute video arranged but certainly for
all the basics for all the basic
sysadmin stuff I'm gonna cover it really
one topic at a time one topic per video
and we're gonna build it up in the way
that we the order that we need to know
it I'm aiming for like
six minute videos so we'll see how close
I get but enjoy I hope you're ready
we're going to turn you into a freakin
hacker
