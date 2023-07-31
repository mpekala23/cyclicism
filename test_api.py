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
            title="The title",
            abstract="The abstract",
            img_url="https://upload.wikimedia.org/wikipedia/commons/b/bd/Test.svg",
            article_url="https://www.nytimes.com/2021/05/02/us/politics/biden-100-days.html",
            date_str="April 1st, 2004"
        ),
        FrontendArticle(
            title="The title",
            abstract="The abstract",
            img_url="https://upload.wikimedia.org/wikipedia/commons/b/bd/Test.svg",
            article_url="https://www.nytimes.com/2021/05/02/us/politics/biden-100-days.html",
            date_str="May 10th, 2023"
        )
    ),
    (
        FrontendArticle(
            title="Trump Crushing DeSantis and G.O.P. Rivals, Times/Siena Poll Finds",
            abstract="The twice-indicted former president leads across nearly every category and region, as primary voters wave off concerns about his escalating legal jeopardy.",
            img_url="images/2023/07/28/multimedia/2023-07-27-july-polls-horserace/2023-07-27-july-polls-horserace-articleLarge-v4.jpg",
            article_url="https://www.nytimes.com/2023/07/31/us/politics/2024-poll-nyt-siena-trump-republicans.html",
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
            title="Why Trump Is So Hard to Beat",
            abstract="The first Times/Siena poll of the G.O.P. primary shows he still commands a seemingly unshakable base of loyal supporters.",
            img_url="images/2023/07/30/upshot/poll-desantis-embed-1690746008551/poll-desantis-embed-1690746008551-articleLarge.png",
            article_url="https://www.nytimes.com/2023/07/31/upshot/poll-trump-republican-primary.html",
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
            title="Homeless Camps Are Being Cleared in California. What Happens Next?",
            abstract="One of the state’s largest homeless encampments was recently shut down in Oakland, but that didn’t stop the problem of homelessness.",
            img_url="images/2023/07/31/multimedia/31nat-homeless-oakland-promo-wbpf/31nat-homeless-oakland-promo-wbpf-articleLarge.jpg",
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
            title="A Climate Warning from the Cradle of Civilization",
            abstract="How extreme temperatures and dwindling water are pushing the Fertile Crescent toward the brink.",
            img_url="images/2023/07/29/multimedia/29iraq-promo-vfpq/29iraq-promo-vfpq-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/29/world/middleeast/iraq-water-crisis-desertification.html",
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
            title="Minor Characters Emerge to Play Key Roles in Trump Documents Case",
            abstract="Carlos De Oliveira and Walt Nauta, who were hired by former President Donald J. Trump despite past troubles, rely on him for their legal fees — and are now his co-defendants.",
            img_url="images/2023/07/30/multimedia/30dc-investigate-chmf/30dc-investigate-chmf-articleLarge-v3.jpg",
            article_url="https://www.nytimes.com/2023/07/30/us/politics/trump-documents-de-oliveira-nauta.html",
            date_str="10-2004"
        ),
        FrontendArticle(
            title="Minor Characters Emerge to Play Key Roles in Trump Documents Case",
            abstract="Carlos De Oliveira and Walt Nauta, who were hired by former President Donald J. Trump despite past troubles, rely on him for their legal fees — and are now his co-defendants.",
            img_url="https://static01.nyt.com/images/2023/07/30/multimedia/30dc-investigate-chmf/30dc-investigate-chmf-superJumbo-v3.jpg",
            article_url="https://www.nytimes.com/2023/07/30/us/politics/trump-documents-de-oliveira-nauta.html",
            date_str="10-2004"
        )
    ),
    (
        FrontendArticle(
            title="Judge Dismisses Trump’s $475 Million Defamation Suit Against CNN",
            abstract="The network’s statements were opinion, the ruling said, and did not support a claim of libel and slander.",
            img_url="images/2023/07/30/multimedia/30trump-lawsuit-1-hwlm/30trump-lawsuit-1-hwlm-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/30/business/media/trump-cnn-lawsuit.html",
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
            title="Trump Team Creates Legal-Defense Fund to Cover His Allies’ Bills",
            abstract="With investigations and legal fees piling up, a fund is planned to help witnesses and defendants. The former president’s legal bills are not expected to be included, however.",
            img_url="images/2023/07/30/multimedia/30pol-legalfund-tcfj/30pol-legalfund-tcfj-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/30/us/politics/trump-legal-defense-fund.html",
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
            title="Why One Country Is Struggling to Break Away From Russian Gas",
            abstract="Austria, unlike most European Union countries, is still buying nearly as much natural gas from Russia as it was before the war in Ukraine.",
            img_url="images/2023/07/31/multimedia/00JPaustria-gas-print-zjcl/00austria-gas-01-zjcl-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/31/business/energy-environment/austria-natural-gas-russia.html",
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
            title="A Trombonist on a Mission to Break Barriers in Classical Music",
            abstract="Hillary Simms is the first woman to become a member of the American Brass Quintet. She says the field needs more role models.",
            img_url="images/2023/07/31/multimedia/30simms-trombone-1/31simms-trombone-dress-fqkh-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/30/arts/music/hillary-simms-american-brass-quintet.html",
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
            title="Inside the Party Switch that Blew Up North Carolina Politics",
            abstract="Tricia Cotham, a Democrat who supported abortion rights, was encouraged to run for a state House seat by powerful Republicans. After she was elected, she joined them and delivered a G.O.P. supermajority.",
            img_url="images/2023/07/27/multimedia/00nat-cotham-01-fjmq/00nat-cotham-01-fjmq-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/30/us/inside-the-party-switch-that-blew-up-north-carolina-politics.html",
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
            title="DeSantis Jabs at Trump’s Legal Trouble as He Resets His Campaign",
            abstract="Ron DeSantis’s remarks to a voter in New Hampshire suggest he may step up his attacks against the man who leads him in national polls by a wide margin.",
            img_url="images/2023/07/30/multimedia/30pol-desantis-qpcg/30pol-desantis-qpcg-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/30/us/desantis-trump-indictments.html",
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
            title="Nuts-and-Bolts Conservatism From Nikki Haley",
            abstract="In her stump speech, the former governor calls for common sense and experience in the White House, leaving crowds wanting more.",
            img_url="images/2023/07/30/multimedia/30pol-haley-fbvj/30pol-haley-fbvj-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/30/us/politics/nikki-haley-stump-speech.html",
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
            title="What Is It About Montecito?",
            abstract="Trying to understand the allure of a place that’s home to Oprah, the self-exiled royals, a celebrity juicer, Katy Perry’s dad — and the New American Dream.",
            img_url="images/2023/07/30/multimedia/30MONTECITO-1-kzch/30MONTECITO-1-kzch-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/30/style/montecito-california.html",
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
            title="Dogs Die From Heat-Related Injuries on Their Way to Police Training",
            abstract="The German shepherds were en route from Chicago to Michigan City, Ind., when the air-conditioning unit in the vehicle in which they were being transported failed, the police said.",
            img_url="images/2023/07/30/multimedia/30xp-dogs-gkfw/30xp-dogs-gkfw-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/30/us/heat-police-dogs-dead-indiana.html",
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
            title="The Lost Art of Fouling the Ball Off (on Purpose)",
            abstract="Spoiling difficult pitches to stay alive was equal parts strategy and party trick. The modern approach to hitting has left it behind.",
            img_url="images/2023/07/28/multimedia/28mlb-foul-balls-promo-fvkq/28mlb-foul-balls-promo-fvkq-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/28/sports/baseball/foul-balls.html",
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
            title="How Trump Could Wreck Things for Republicans in 2024",
            abstract="The governor’s race in New Hampshire offers a window into the ways Trump could complicate the lives of down-ballot G.O.P. candidates.",
            img_url="images/2023/07/30/multimedia/30cottle-mtlz/30cottle-mtlz-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/30/opinion/donald-trump-new-hampshire.html",
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
            title="What ‘Oppenheimer’ Doesn’t Tell You About the Trinity Test",
            abstract="As a new generation of Americans learns about the world’s first nuclear test, the people who lived through it are being left out of the story again.",
            img_url="images/2023/07/31/opinion/23cordova-1/23cordova-1-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/30/opinion/international-world/oppenheimer-nuclear-bomb-cancer.html",
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
            title="The Research Scandal at Stanford Is More Common Than You Think",
            abstract="Scientific journals need to harden their defenses against research manipulation.",
            img_url="images/2023/07/30/multimedia/30baker-planb-image-bkmz/30baker-planb-image-bkmz-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/30/opinion/stanford-president-student-journalist.html",
            date_str="06-2005"
        ),
        FrontendArticle(
            title="The Research Scandal at Stanford Is More Common Than You Think",
            abstract="Scientific journals need to harden their defenses against research manipulation.",
            img_url="https://static01.nyt.com/images/2023/07/30/multimedia/30baker-planb-image-bkmz/30baker-planb-image-bkmz-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/30/opinion/stanford-president-student-journalist.html",
            date_str="06-2005"
        )
    ),
    (
        FrontendArticle(
            title="It Was Never Just About the Butterflies",
            abstract="Make very little of yourself if you wish to see clearly. Shut up, deeply, if you wish to hear.",
            img_url="images/2023/07/30/opinion/30hyde/30hyde-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/30/opinion/butterfly-hunting-attention.html",
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
            title="Excavations Uncover Hints of Nero’s Theater in Rome, and Much More",
            abstract="A dig at a palace set to become a hotel has unearthed traces of a theater that archaeologists hypothesize was built by Nero, the emperor with a disputed reputation for tyranny and debauchery.",
            img_url="images/2023/07/31/multimedia/31italy-nero-01-htwv/00italy-nero-01-htwv-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/30/world/europe/rome-nero-theater.html",
            date_str="04-2001"
        ),
        FrontendArticle(
            title="Excavations Uncover Hints of Nero’s Theater in Rome, and Much More",
            abstract="A dig at a palace set to become a hotel has unearthed traces of a theater that archaeologists hypothesize was built by Nero, the emperor with a disputed reputation for tyranny and debauchery.",
            img_url="https://static01.nyt.com/images/2023/07/31/multimedia/31italy-nero-01-htwv/00italy-nero-01-htwv-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/30/world/europe/rome-nero-theater.html",
            date_str="04-2001"
        )
    ),
    (
        FrontendArticle(
            title="At Least 43 Killed in Blast at Political Rally in Pakistan",
            abstract="An explosion at a political rally on Sunday in northwest Pakistan killed dozens of people and injured 200 more, officials said, the latest sign of the deteriorating security situation in Pakistan, where some militant groups have become more active over the past two years.",
            img_url="images/2023/07/30/multimedia/30Pakistan-04-jlzg/30Pakistan-04-jlzg-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/30/world/asia/pakistan-rally-explosion.html",
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
    (
        FrontendArticle(
            title="Tide of Terror Shifts in Haiti as U.S. Nurse and Her Child Are Abducted",
            abstract="This, along with other recent kidnappings, may signal the end of a brief respite, as gangs tighten their grip after being targets of vigilante violence.",
            img_url="images/2023/07/31/multimedia/31haiti-kidnap-ktgv/31haiti-kidnap-ktgv-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/31/world/americas/haiti-kidnapping-nurse.html",
            date_str="02-2003"
        ),
        FrontendArticle(
            title="Tide of Terror Shifts in Haiti as U.S. Nurse and Her Child Are Abducted",
            abstract="This, along with other recent kidnappings, may signal the end of a brief respite, as gangs tighten their grip after being targets of vigilante violence.",
            img_url="https://static01.nyt.com/images/2023/07/31/multimedia/31haiti-kidnap-ktgv/31haiti-kidnap-ktgv-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/31/world/americas/haiti-kidnapping-nurse.html",
            date_str="02-2003"
        )
    ),
    (
        FrontendArticle(
            title="Driver Plows Car Into Migrant Workers in ‘Intentional Assault,’ Police Say",
            abstract="The vehicle cut over a median and toward where the six workers were standing outside a Walmart in Lincolnton, N.C., the police said. The authorities were looking for the driver.",
            img_url="images/2023/07/30/multimedia/30xp-migrants/30xp-migrants-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/31/us/migrant-workers-lincolnton-crash.html",
            date_str="12-2003"
        ),
        FrontendArticle(
            title="Driver Plows Car Into Migrant Workers in ‘Intentional Assault,’ Police Say",
            abstract="The vehicle cut over a median and toward where the six workers were standing outside a Walmart in Lincolnton, N.C., the police said. The authorities were looking for the driver.",
            img_url="https://static01.nyt.com/images/2023/07/30/multimedia/30xp-migrants/30xp-migrants-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/31/us/migrant-workers-lincolnton-crash.html",
            date_str="12-2003"
        )
    ),
    (
        FrontendArticle(
            title="A High-Water Year for River Rafting",
            abstract="All that snow in the West? It’s water now, and it’s providing a banner season for white-water rafting. Here are five rivers to run this summer.",
            img_url="images/2023/07/27/travel/oakImage-1690478550240/oakImage-1690478550240-articleLarge.jpg",
            article_url="https://www.nytimes.com/2023/07/28/travel/white-water-rafting-rivers.html",
            date_str="03-2003"
        ),
        FrontendArticle(
            title="A High-Water Year for River Rafting",
            abstract="All that snow in the West? It’s water now, and it’s providing a banner season for white-water rafting. Here are five rivers to run this summer.",
            img_url="https://static01.nyt.com/images/2023/07/27/travel/oakImage-1690478550240/oakImage-1690478550240-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/07/28/travel/white-water-rafting-rivers.html",
            date_str="03-2003"
        )
    ),
]

@app.route("/")
def index():
    return render_template("index.html", results=results * 10)
