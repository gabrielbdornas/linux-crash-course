welcome to part 2 this is just going to
be some housekeeping stuff I say that
because not everyone who wants to take a
look at this tutorial and follow along
and you absolutely have to follow along
to really learn this stuff some people
aren't going to want to jump in and like
replace their current operating system
whether it's Windows or Mac OS in most
cases with Linux and I understand and
even things that are pretty easy now
like dual booting so setting up a Linux
operating system next to your Windows or
Mac OS X operating system and then
choosing at boot which one you want to
go into that can still be a little scary
for some people so I'm just going to
talk about an alternative here and show
you how to do it there is another
alternative obviously which is just
taking an old computer like a laptop or
an old desktop and installing just Linux
on that but I find that it's nice to
have on your primary machine so that
you're always kind of motivated to be
using it ok so the way we're going to do
it is we're going to install Linux as a
virtual machine or a VM and what that is
is basically it's an application on your
computer which will basically create an
environment for another operating system
to run just like any other application
and so that operating system in this
case Linux won't know that it's not on a
physical machine there's two parts to
this first we download the operating
system then we download the the
VirtualBox software so the software
that's going to let us install that
operating system on your machine now
without touching your current operating
system and then I'll show you how to
install it and that install process will
be just about the same whether you're
doing it in a virtual machine or on a
real computer ok so step one is going to
the Linux distributions website now
there's lots of different distributions
I'm going to use Ubuntu here not because
I think it's the best one but because
it's extremely popular extremely well
supported so you're going to basically
see it everywhere if you want to work
with Linux you're going to run into this
and you need to be prepared it's not my
favorite distribution but you should
know it
okay so Butch's website is Ubuntu calm
and just skip all the marketing and go
to slash download slash desktop I
debated on whether or not to use a
server operating system they they have a
server version without a graphical user
interface as well but just for just for
ease of use we're going to go with the
desktop version we're going to be
spending most of our time in the
terminal though this is not going to be
like how to use office on Linux or
something okay
so go ahead and start the download you
don't care about extended support
versions so just scroll down for the
latest one this might be 1310 if it's
later in the year it'll be 14
what is it 14 4 wow yeah
every six months a new version comes out
but it's not really I mean it's just
sort of updated binaries it doesn't
matter so choose the download they're
going to ask you for money but you don't
have to pay any money so just scroll to
the bottom and say no thanks canonical
the download will start just click OK
okay our second move is going to
virtualbox.org this is an Oracle project
and this is what's going to allow us to
run a virtual machine so go to
virtualbox.org click on downloads and
just download one of these binaries
you're probably most likely on a Windows
machine so you'll download this so
download here just click save file just
like Ubuntu and then just wait for the
Downloads to complete
okay our downloads have completed so
just go ahead and install VirtualBox it
will ask you a bunch of times if you
want to authorize software by Oracle
blah blah blah virtual adapters blah
blah blah technical stuff just keep
clicking yes what this is going to do is
it's going to create sort of virtual
devices and virtual adapters on your
Windows or Mac machine that your virtual
machines can use to do things like
interface with your network so you can
have internet access on them good so
presuming you've got VirtualBox
installed click new to create a new
machine and we'll just call this a
learning and it correctly guesses that
we're using Linux this is your like old
kernels we'll just say oh there we go
Wow it even has one two we will hit next
and it will last how much memory we want
to give it I'm going to give this it's
2048 so just about two gigs click next
we'll create a new virtual hard drive
this is fine so just hit next
dynamically I'll cut it just means that
it's not going to take a chunk of hard
drive space right now it will simply
slowly grow as a file or set of files on
your disk as you approach the limit that
you're going to set here I think 8 gigs
is just about
fine more than enough you could probably
get away for what we're doing with
something like four gigs so double click
to power the machine on or you can just
hit start and here you're going to click
and navigate to the image you just
downloaded it so it can boot from that
select that ok hit start so it's going
to boot up from that install CD or live
CD if you're having trouble with this
just google around or search around for
you know VirtualBox and then whatever
error you're seeing on the screen
because there's a million people who try
this without turning on their
virtualization support and you'll get it
fixed quickly this is just some software
licensing crap I would install
third-party software and if you're
really going to be using this as a work
machine they're not just a learning
machine you can go ahead and download
updates but I don't care about that
we're going to erase the disk and
install Ubuntu if you're going to do
this on a machine for actually working
on if you really want to make Linux your
main operating system which by the way
is a great idea if you really want to
learn it I would recommend checking both
of these boxes so using LVM on the disc
that's the the logical volume manager
manager for linux what that does is it
basically just abstracts storage from
being like physical things like
partitions which are kind of annoying to
resize once you have them and they're
like correspond like physical locations
on the disk and this abstracts that so
you create these abstract volumes that
are on the partitions and these are very
easy to like if you want to shrink or or
enlarge them I was going to say and
bigan which is one of my favorite word's
but unfortunately doesn't exist so if
you want to shrink or in big in these
these logical partitions these logical
volumes later you can do that very
easily and what it does is underneath
it'll just create a new physical
partitioner
or add to the size of one but it sort of
frees you from having to deal with that
going to yourself it's also much faster
um and I would also encrypt it just
because you should just be encrypting
stuff by default it's just like hello I
would like some privacy and that will
ensure that whatever you put inside that
logical volume so your entire operating
system most of it will be encrypted and
so if someone just like matches your
computer open and steals your hard drive
they won't be able to get any of your
personal data from it you know you just
won't have any problems you can these
aren't like the one doesn't depend on
the other so you can just encrypt it and
not use LVM you get just use LVM and not
encrypt it doesn't matter okay but we're
just going to erase this disk in assault
but do it because we're lazy and this is
just for learning I am in Austria right
now believe it or not if you get dead by
my accent and my love for violent
violent operating systems all right
American layout and we'll just choose a
name
so there's 2z username and password and
if you already using full disk
encryption you don't need to do this but
if you're not if you didn't choose
encrypt the disk before so if you're not
using Lux in this case just cook your
home folder because that again prevents
that that nasty someone stole my
computer and they have access to all my
data no problem but we don't need that
because this is just a learning machine
getting tired of hearing that for God's
sake I mean justjust know this is all
this add-on crap that would you tries to
sell you oh hello there I'm so sorry you
caught me looking at one of my favorite
games good that's enough for a
recommendation
once you're done installing just restart
the old machine ok so you've now got a
working Linux machine running in a
virtual machine good I hope you enjoyed
