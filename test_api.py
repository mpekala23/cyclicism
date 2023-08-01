# THIS IS AN AUTO-GENERATED FILE. DO NOT EDIT
from flask import Flask, render_template
from typing import Union, NamedTuple

app = Flask(__name__)


class FrontendArticle(NamedTuple):
    title: str
    abstract: str
    img_url: Union[str, None]
    article_url: str
    date_str: str


results = [
    (
        FrontendArticle(
            title="The Early Word: Florida Preps for Debate",
            abstract="Faced with sliding poll numbers in Florida, Rudolph W. Giuliani has been speaking more and more about the economy — sure to be a hot topic at tonight’s Republican debate in Boca Raton.",
            img_url="None",
            article_url="https://thecaucus.blogs.nytimes.com/2008/01/24/the-early-word-florida-preps-for-debate/",
            date_str="06-2001"
        ),
        FrontendArticle(
            title="Trump Crushing DeSantis and G.O.P. Rivals, Times/Siena Poll Finds",
            abstract="The twice-indicted former president leads across nearly every category and region, as primary voters wave off concerns about his escalating legal jeopardy.",
            img_url="https://static01.nyt.com/images/2023/07/28/multimedia/2023-07-27-july-polls-horserace/2023-07-27-july-polls-horserace-superJumbo-v4.jpg",
            article_url="https://www.nytimes.com/2023/07/31/us/politics/2024-poll-nyt-siena-trump-republicans.html",
            date_str="06-2001"
        )
    ),
    (
        FrontendArticle(
            title="Protests Spur Surge in Donations, Giving ActBlue Its Biggest Day of the Year",
            abstract="With money flowing to candidates, bail funds and charities, the Democrats’ online donor platform processed over $60 million between Friday and Monday, a sign of strength for the party.",
            img_url="https://static01.nyt.com/images/2020/06/04/style/01unrest-donations/merlin_173050722_79a799e1-a17c-4c84-97cd-ce22c60101a6-articleLarge.jpg",
            article_url="https://www.nytimes.com/2020/06/01/us/politics/donations-protests-actblue-democrats.html",
            date_str="04-2002"
        ),
        FrontendArticle(
            title="Why Trump Is So Hard to Beat",
            abstract="The first Times/Siena poll of the G.O.P. primary shows he still commands a seemingly unshakable base of loyal supporters.",
            img_url="https://static01.nyt.com/images/2023/07/30/upshot/poll-desantis-embed-1690746008551/poll-desantis-embed-1690746008551-superJumbo.png",
            article_url="https://www.nytimes.com/2023/07/31/upshot/poll-trump-republican-primary.html",
            date_str="04-2002"
        )
    ),
    (
        FrontendArticle(
            title="Obama Says Bush and McCain Are ‘Fear Mongering’ in Attacks",
            abstract="Senator Barack Obama responded to attacks on his foreign policy and tried to turn the tables on his critics.",
            img_url="https://static01.nyt.com/images/2008/05/17/us/politics/17obama.span.jpg",
            article_url="https://www.nytimes.com/2008/05/17/us/politics/17obama.html",
            date_str="02-2004"
        ),
        FrontendArticle(
            title="DeSantis Jabs at Trump’s Legal Trouble as He Resets His Campaign",
            abstract="Ron DeSantis’s remarks to a voter in New Hampshire suggest he may step up his attacks against the man who leads him in national polls by a wide margin.",
            img_url="https://static01.nyt.com/images/2023/07/30/multimedia/30pol-desantis-qpcg/30pol-desantis-qpcg-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/30/us/desantis-trump-indictments.html",
            date_str="02-2004"
        )
    ),
    (
        FrontendArticle(
            title="‘Condoleezza Rice’",
            abstract="“The story of Condoleezza Rice begins at the close of the nineteenth century on a cotton plantation in southeastern Alabama, near the flourishing little town of Union Springs.”",
            img_url="https://static01.nyt.com/images/2007/12/27/arts/elisabeth-bumiller-190.jpg",
            article_url="https://www.nytimes.com/2008/01/20/books/chapters/1st-chapter-bumiller-condoleezza-rice.html",
            date_str="11-2004"
        ),
        FrontendArticle(
            title="Nuts-and-Bolts Conservatism From Nikki Haley",
            abstract="In her stump speech, the former governor calls for common sense and experience in the White House, leaving crowds wanting more.",
            img_url="https://static01.nyt.com/images/2023/07/30/multimedia/30pol-haley-fbvj/30pol-haley-fbvj-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/30/us/politics/nikki-haley-stump-speech.html",
            date_str="11-2004"
        )
    ),
    (
        FrontendArticle(
            title="Homeless Camps Are Being Cleared in California. What Happens Next?",
            abstract="One of the state’s largest homeless encampments was recently shut down in Oakland, but that didn’t stop the problem of homelessness.",
            img_url="https://static01.nyt.com/images/2023/07/31/multimedia/31nat-homeless-oakland-promo-wbpf/31nat-homeless-oakland-promo-wbpf-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/30/us/homeless-camp-oakland-california.html",
            date_str="01-2002"
        ),
        FrontendArticle(
            title="Homeless Camps Are Being Cleared in California. What Happens Next?",
            abstract="One of the state’s largest homeless encampments was recently shut down in Oakland, but that didn’t stop the problem of homelessness.",
            img_url="https://static01.nyt.com/images/2023/07/31/multimedia/31nat-homeless-oakland-promo-wbpf/31nat-homeless-oakland-promo-wbpf-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/30/us/homeless-camp-oakland-california.html",
            date_str="01-2002"
        )
    ),
    (
        FrontendArticle(
            title="Scientists Warn of Perilous Climate Shift Within Decades, Not Centuries",
            abstract="Findings published on Tuesday are likely to replay a debate among climate scientists that started when a draft version of the paper came out last year.",
            img_url="https://static01.nyt.com/images/2016/03/22/science/22CLIMATE/22CLIMATE-watch308.jpg",
            article_url="https://www.nytimes.com/2016/03/23/science/global-warming-sea-level-carbon-dioxide-emissions.html",
            date_str="12-2001"
        ),
        FrontendArticle(
            title="A Climate Warning from the Cradle of Civilization",
            abstract="How extreme temperatures and dwindling water are pushing the Fertile Crescent toward the brink.",
            img_url="https://static01.nyt.com/images/2023/07/29/multimedia/29iraq-promo-vfpq/29iraq-promo-vfpq-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/29/world/middleeast/iraq-water-crisis-desertification.html",
            date_str="12-2001"
        )
    ),
    (
        FrontendArticle(
            title="How Rupert Murdoch’s Empire of Influence Remade the World",
            abstract="Murdoch and his children have toppled governments on two continents and destabilized the most important democracy on Earth. What do they want?",
            img_url="https://static01.nyt.com/images/2019/04/07/magazine/07mag-murdoch-promo-image-1/07mag-murdoch-promo-image-1-articleLarge.jpg",
            article_url="https://www.nytimes.com/interactive/2019/04/03/magazine/rupert-murdoch-fox-news-trump.html",
            date_str="05-2003"
        ),
        FrontendArticle(
            title="Judge Dismisses Trump’s $475 Million Defamation Suit Against CNN",
            abstract="The network’s statements were opinion, the ruling said, and did not support a claim of libel and slander.",
            img_url="https://static01.nyt.com/images/2023/07/30/multimedia/30trump-lawsuit-1-hwlm/30trump-lawsuit-1-hwlm-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/30/business/media/trump-cnn-lawsuit.html",
            date_str="05-2003"
        )
    ),
    (
        FrontendArticle(
            title="The Songs That Get Us Through It",
            abstract="Featuring music from Mary J. Blige, Olivia Rodrigo, Beach House, Mitski and more.",
            img_url="https://static01.nyt.com/images/2022/03/13/magazine/13mag-music-promoimage/13mag-music-promoimage-articleLarge-v2.png",
            article_url="https://www.nytimes.com/interactive/2022/03/11/magazine/best-songs.html",
            date_str="12-2003"
        ),
        FrontendArticle(
            title="Trump Team Creates Legal-Defense Fund to Cover His Allies’ Bills",
            abstract="With investigations and legal fees piling up, a fund is planned to help witnesses and defendants. The former president’s legal bills are not expected to be included, however.",
            img_url="https://static01.nyt.com/images/2023/07/30/multimedia/30pol-legalfund-tcfj/30pol-legalfund-tcfj-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/30/us/politics/trump-legal-defense-fund.html",
            date_str="12-2003"
        )
    ),
    (
        FrontendArticle(
            title="At the Time Warner Center, an Enclave of Powerful Russians",
            abstract="Wealth that has been accrued in the chaotic capitalism of post-Soviet Russia is a powerful force in the luxury condominium boom that is changing New York.",
            img_url="https://static01.nyt.com/images/2015/01/16/us/xxRUSSIA1/xxRUSSIA1-watch308.jpg",
            article_url="https://www.nytimes.com/2015/02/12/nyregion/russia-time-warner-center-andrey-vavilov.html",
            date_str="11-2002"
        ),
        FrontendArticle(
            title="Why One Country Is Struggling to Break Away From Russian Gas",
            abstract="Austria, unlike most European Union countries, is still buying nearly as much natural gas from Russia as it was before the war in Ukraine.",
            img_url="https://static01.nyt.com/images/2023/07/31/multimedia/00JPaustria-gas-print-zjcl/00austria-gas-01-zjcl-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/31/business/energy-environment/austria-natural-gas-russia.html",
            date_str="11-2002"
        )
    ),
    (
        FrontendArticle(
            title="Hundreds of New Concertos Bring the World to the Concert Hall",
            abstract="Dai Fujikura’s new work for shamisen, a three-stringed, fretless Japanese lute, premieres on Saturday.",
            img_url="https://static01.nyt.com/images/2019/08/03/arts/02SHAMISEN-1/merlin_158733756_81f777fd-9a99-40ab-a994-2fbed4c636e5-articleLarge.jpg",
            article_url="https://www.nytimes.com/2019/08/01/arts/music/lincoln-center-dai-fujikura-shamisen.html",
            date_str="12-2005"
        ),
        FrontendArticle(
            title="A Trombonist on a Mission to Break Barriers in Classical Music",
            abstract="Hillary Simms is the first woman to become a member of the American Brass Quintet. She says the field needs more role models.",
            img_url="https://static01.nyt.com/images/2023/07/31/multimedia/30simms-trombone-1/31simms-trombone-dress-fqkh-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/30/arts/music/hillary-simms-american-brass-quintet.html",
            date_str="12-2005"
        )
    ),
    (
        FrontendArticle(
            title="North Korea, Wells Fargo, Serena Williams: Your Friday Briefing",
            abstract="Here’s what you need to know to start your day.",
            img_url="https://static01.nyt.com/images/2016/09/10/nytnow/09NYTNow-Korea1/09NYTNow-Korea1-hpLarge-v2.jpg",
            article_url="https://www.nytimes.com/2016/09/09/briefing/north-korea-wells-fargo-serena-williams.html",
            date_str="05-2001"
        ),
        FrontendArticle(
            title="Inside the Party Switch that Blew Up North Carolina Politics",
            abstract="Tricia Cotham, a Democrat who supported abortion rights, was encouraged to run for a state House seat by powerful Republicans. After she was elected, she joined them and delivered a G.O.P. supermajority.",
            img_url="https://static01.nyt.com/images/2023/07/27/multimedia/00nat-cotham-01-fjmq/00nat-cotham-01-fjmq-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/30/us/inside-the-party-switch-that-blew-up-north-carolina-politics.html",
            date_str="05-2001"
        )
    ),
    (
        FrontendArticle(
            title="Out of the Loss of a Garden, Another Life Lesson",
            abstract="When Joan Dye Gussow, nutritionist and matriarch of the eat-locally-think-globally food movement, lost her vegetable garden, she took the opportunity to reinvent it.",
            img_url="https://static01.nyt.com/images/2010/08/19/garden/19gardenspan-1/jpGARDEN1-articleLarge.jpg",
            article_url="https://www.nytimes.com/2010/08/19/garden/19garden.html",
            date_str="12-2002"
        ),
        FrontendArticle(
            title="What Is It About Montecito?",
            abstract="Trying to understand the allure of a place that’s home to Oprah, the self-exiled royals, a celebrity juicer, Katy Perry’s dad — and the New American Dream.",
            img_url="https://static01.nyt.com/images/2023/07/30/multimedia/30MONTECITO-1-kzch/30MONTECITO-1-kzch-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/30/style/montecito-california.html",
            date_str="12-2002"
        )
    ),
    (
        FrontendArticle(
            title="Rakesses, Writers, Activists and Dukes, All of Them Hot",
            abstract="Does the state of the world have you desperate for a happy ending? Pick up a romance novel.",
            img_url="https://static01.nyt.com/images/2020/05/31/books/review/31Romance-GREEN/31Romance-GREEN-articleLarge-v3.jpg",
            article_url="https://www.nytimes.com/interactive/2020/books/romance-novels-summer.html",
            date_str="02-2001"
        ),
        FrontendArticle(
            title="Dogs Die From Heat-Related Injuries on Their Way to Police Training",
            abstract="The German shepherds were en route from Chicago to Michigan City, Ind., when the air-conditioning unit in the vehicle in which they were being transported failed, the police said.",
            img_url="https://static01.nyt.com/images/2023/07/30/multimedia/30xp-dogs-gkfw/30xp-dogs-gkfw-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/30/us/heat-police-dogs-dead-indiana.html",
            date_str="02-2001"
        )
    ),
    (
        FrontendArticle(
            title="For Field Hockey, an Encouraging First Game",
            abstract="The United States field hockey team lost its first game to Germany, but its athleticism and aggressive attack were impressive.",
            img_url="None",
            article_url="https://london2012.blogs.nytimes.com/2012/07/30/for-field-hockey-an-encouraging-first-game/",
            date_str="08-2004"
        ),
        FrontendArticle(
            title="The Lost Art of Fouling the Ball Off (on Purpose)",
            abstract="Spoiling difficult pitches to stay alive was equal parts strategy and party trick. The modern approach to hitting has left it behind.",
            img_url="https://static01.nyt.com/images/2023/07/28/multimedia/28mlb-foul-balls-promo-fvkq/28mlb-foul-balls-promo-fvkq-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/28/sports/baseball/foul-balls.html",
            date_str="08-2004"
        )
    ),
    (
        FrontendArticle(
            title="Who’s Minding the Schools?",
            abstract="Are new standards really leveling the playing field? Or is the game prearranged so that many, if not most, of the players will fail?",
            img_url="https://static01.nyt.com/images/2013/06/09/sunday-review/09CORE/09CORE-thumbWide-v2.jpg",
            article_url="https://www.nytimes.com/2013/06/09/opinion/sunday/the-common-core-whos-minding-the-schools.html",
            date_str="06-2001"
        ),
        FrontendArticle(
            title="How Trump Could Wreck Things for Republicans in 2024",
            abstract="The governor’s race in New Hampshire offers a window into the ways Trump could complicate the lives of down-ballot G.O.P. candidates.",
            img_url="https://static01.nyt.com/images/2023/07/30/multimedia/30cottle-mtlz/30cottle-mtlz-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/30/opinion/donald-trump-new-hampshire.html",
            date_str="06-2001"
        )
    ),
    (
        FrontendArticle(
            title="Senate Report Details Jan. 6 Intelligence and Law Enforcement Failures",
            abstract="The report by Democrats provided the most comprehensive picture to date of how federal officials missed, downplayed or failed to act on multiple threats of and plans for violence.",
            img_url="https://static01.nyt.com/images/2023/06/27/multimedia/27dc-Jan6-gzhw/27dc-Jan6-gzhw-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/06/27/us/politics/jan-6-report-senate.html",
            date_str="10-2004"
        ),
        FrontendArticle(
            title="What ‘Oppenheimer’ Doesn’t Tell You About the Trinity Test",
            abstract="As a new generation of Americans learns about the world’s first nuclear test, the people who lived through it are being left out of the story again.",
            img_url="https://static01.nyt.com/images/2023/07/31/opinion/23cordova-1/23cordova-1-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/30/opinion/international-world/oppenheimer-nuclear-bomb-cancer.html",
            date_str="10-2004"
        )
    ),
    (
        FrontendArticle(
            title="What Can I Do to Lighten Up Thanksgiving?",
            abstract="There are various ways to approach this question. If you’re talking about the food, it’s possible that your crusade is a hopeless one, sort of like striving to snuff out the noise of fireworks on the 4th of July or giving kids homemade agave-nectar granola clusters on Halloween. But if, instead, your question has more to do with bringing a breeze of social and mental lightness to the holiday proceedings, we’d like to recommend the “Thin Man” approach.",
            img_url="None",
            article_url="https://dinersjournal.blogs.nytimes.com/2011/11/23/what-can-i-do-to-lighten-up-thanksgiving/",
            date_str="04-2004"
        ),
        FrontendArticle(
            title="It Was Never Just About the Butterflies",
            abstract="Make very little of yourself if you wish to see clearly. Shut up, deeply, if you wish to hear.",
            img_url="https://static01.nyt.com/images/2023/07/30/opinion/30hyde/30hyde-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/30/opinion/butterfly-hunting-attention.html",
            date_str="04-2004"
        )
    ),
    (
        FrontendArticle(
            title="Bombing at Hotel in Pakistan Kills at Least 40",
            abstract="A huge truck bombing at Islamabad’s Marriott Hotel was one of the worst acts of terrorism in Pakistan’s history.",
            img_url="https://static01.nyt.com/images/2008/09/21/world/21pakistan.xlarge1.jpg",
            article_url="https://www.nytimes.com/2008/09/21/world/asia/21islamabad.html",
            date_str="03-2004"
        ),
        FrontendArticle(
            title="At Least 43 Killed in Blast at Political Rally in Pakistan",
            abstract="An explosion at a political rally on Sunday in northwest Pakistan killed dozens of people and injured 200 more, officials said, the latest sign of the deteriorating security situation in Pakistan, where some militant groups have become more active over the past two years.",
            img_url="https://static01.nyt.com/images/2023/07/30/multimedia/30Pakistan-04-jlzg/30Pakistan-04-jlzg-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/30/world/asia/pakistan-rally-explosion.html",
            date_str="03-2004"
        )
    ),
]

@app.route("/")
def index():
    return render_template("index.html", results=results * 10)
