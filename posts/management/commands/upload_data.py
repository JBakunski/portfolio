from django.core.management.base import BaseCommand
from posts.models import Author, Post


class Command(BaseCommand):
    def handle(self, *args, **options):
        a1 = Author.objects.create(nick='Rutek', email='dobromil.rutkowski@jourrapide.com')
        a2 = Author.objects.create(nick='Jędrek', email='jedrzejadmaski@armyspy.com',
                                   bio='''When you write a first-person bio you're telling your story 
                                    directly to your audience. This shows them that you crafted your bio 
                                    with your personal experience and opinions.''')
        a3 = Author.objects.create(nick='Nowa', email='wislawa.nowak@teleworm.us')

        Post.objects.bulk_create(
            [Post(title='The Cheesecake Factory: Use humor and great photos',
                  content='''The Cheesecake Factory is an American chain of restaurants, 
                  localized around the world. If youre not familiar with it, 
                  you may recognize the name from the hit series The Big Bang Theory. 
                  They have a large following on Facebook and regularly post about food 
                  thats on their menu. These posts get a lot of engagement, due to the 
                  great images used and the funny text accompanying them.''', author=a2),
            Post(title='Google: Share interesting customer stories',
                  content='''Google Maps is one of those things that doesnt need much explaining. 
                  Most people know what it does, it helps you get from A to B. It can even find you 
                  a faster route when theres loads of traffic up ahead. But a few days back, Google 
                  shared an interesting customer story on Twitter.''', author=a1),
            Post(title='Tonys Chocolonely: Show people whats happening',
                  content='''Tony Chocolonely is a Dutch company that sells chocolate. Their chocolate
                   bars are quite popular and their mission is to make chocolate 100% slave-free. As they 
                   are opinionated, which fits their mission, they often get a lot of engagement on their 
                   social posts.''', author=a1),
            Post(title='The Clay Creative Co: Increase followers with giveaways',
                  content='''Now, this is an online store youve probably not heard of, as its a small
                   business from the UK that sells its earrings through Etsy. But 
                   this post on Instagram is a great example of how a small online business 
                   can grow its number of followers. By doing a simple giveaway!''', author=a3)]
        )

        self.stdout.write(self.style.SUCCESS("Database successfully updated"))