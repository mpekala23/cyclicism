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
            title="Deal Ends Possibility Of Clinton Indictment",
            abstract="WASHINGTON—  Bill Clinton and the independent counsel investigating him announced an agreement Friday to clear Mr. Clinton from lingering legal jeopardy in the sexual scandals that marred his presidency, but only at the cost of an embarrassing admission by the president on his last full day in office that he had misled an Arkansas court. ",
            img_url=None,
            article_url="https://www.nytimes.com/2001/01/20/news/deal-ends-possibility-of-clinton-indictment.html",
            date_str="January 2001",
        ),
        FrontendArticle(
            title="Trump, Arraigned on Election Charges, Pleads Not Guilty",
            abstract="The former president appeared in federal court in Washington after being indicted over his efforts to overturn his defeat in 2020. His first pretrial hearing was set for Aug. 28.",
            img_url="https://static01.nyt.com/images/2023/08/03/multimedia/03d-trump-pjkc/03d-trump-pjkc-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/08/03/us/politics/trump-arraignment-court.html",
            date_str="August 2023",
        ),
    ),
    (
        FrontendArticle(
            title="Schwarz Jury Asks a Question but Reaches No Verdict on First Day",
            abstract="Jury in retrial of former New York City police officer Charles Schwarz adjourns after first day of deliberations without verdict; Schwarz faces two perjury charges and two civil rights charges that assert he assisted officer Justin A Volpe in assaulting Abner Louima in bathroom of police station house in 1997; photo (M)",
            img_url=None,
            article_url="https://www.nytimes.com/2002/07/10/nyregion/schwarz-jury-asks-a-question-but-reaches-no-verdict-on-first-day.html",
            date_str="July 2002",
        ),
        FrontendArticle(
            title="Trump’s day in court included another encounter with Jack Smith, but no eye contact.",
            abstract="This time the seriousness of the charges facing the former president gave the proceedings a sense of historical weight.",
            img_url="https://static01.nyt.com/images/2023/08/03/multimedia/03trump-blog-scene-fqpg/03trump-blog-scene-fqpg-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/08/03/us/politics/trump-court-appearance-arraignment.html",
            date_str="August 2023",
        ),
    ),
    (
        FrontendArticle(
            title="The Senate, the Filibuster and the Judges",
            abstract="John Prior letter says he is not opposed to filibustering and supports requirement calling for 60 votes to confirm judicial nominees (Mar 29 editorial)",
            img_url=None,
            article_url="https://www.nytimes.com/2005/04/04/opinion/the-senate-the-filibuster-and-the-judges-687472.html",
            date_str="April 2005",
        ),
        FrontendArticle(
            title="Four takeaways from Trump’s court appearance.",
            abstract="A quick proceeding that was mostly straightforward.",
            img_url="https://static01.nyt.com/images/2023/08/03/multimedia/03trump-arraignment-election-takeaways-02-qgzt/03trump-arraignment-election-takeaways-02-qgzt-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/08/03/us/politics/trump-arraignment-takeaways.html",
            date_str="August 2023",
        ),
    ),
    (
        FrontendArticle(
            title="Democrat Pulls Her Support For Senate Malpractice Bill",
            abstract="Sen Dianne Fenstein, Democrat who has been working with majority leader Sen Bill Frist and other Republican leaders on compromise measure to limit jury awards in medical malpractice suits, says she is withdrawing her name from legislation in face of American Medical Assn opposition; photo (M)",
            img_url=None,
            article_url="https://www.nytimes.com/2003/03/27/us/democrat-pulls-her-support-for-senate-malpractice-bill.html",
            date_str="March 2003",
        ),
        FrontendArticle(
            title="For an Ailing Feinstein, a Fight Over the Family Fortune",
            abstract="As Dianne Feinstein, 90, struggles to function in the Senate, a dispute within her family over control of her late husband’s estate is another difficult chapter at the end of a long career.",
            img_url="https://static01.nyt.com/images/2023/08/01/multimedia/01NAT-FEINSTEIN-01-lmhg/01NAT-FEINSTEIN-01-lmhg-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/08/03/us/feinstein-husband-estate-family-fortune.html",
            date_str="August 2023",
        ),
    ),
    (
        FrontendArticle(
            title="2 Men Get Stiff Sentences in China Over Worker Protests",
            abstract="Two men who promoted large worker protests in northeast China 14 months ago have been given stiff prison sentences, of seven and four years, on charges of subverting the state.",
            img_url=None,
            article_url="https://www.nytimes.com/2003/05/09/international/asia/2-men-get-stiff-sentences-in-china-over-worker-protests.html",
            date_str="May 2003",
        ),
        FrontendArticle(
            title="Two U.S. Navy Sailors Charged With Helping China",
            abstract="Prosecutors said the two sailors in California gave Chinese intelligence officers U.S. military secrets and sensitive information.",
            img_url="https://static01.nyt.com/images/2023/08/03/multimedia/03dc-intel-01a-gwht/03dc-intel-01a-gwht-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/08/03/us/politics/navy-sailors-spy-china.html",
            date_str="August 2023",
        ),
    ),
    (
        FrontendArticle(
            title="Affirmative Action: The Ruling and the Debate",
            abstract="Elliott Marc Davis letter scores Supreme Court decision on affirmative action; says true equality of opportunity would give preference to underprivileged, deserving students of all colors and creeds (Jun 24 editorial)",
            img_url=None,
            article_url="https://www.nytimes.com/2003/06/25/opinion/l-affirmative-action-the-ruling-and-the-debate-258130.html",
            date_str="June 2003",
        ),
        FrontendArticle(
            title="The Next Affirmative Action Battle May Be at West Point",
            abstract="Students for Fair Admissions won its Supreme Court case against Harvard and the University of North Carolina. Now, it’s focusing on a possible new target: the military academies.",
            img_url="https://static01.nyt.com/images/2023/08/03/multimedia/03NAT-AFFIRMATIVEACTION-02-glhf/03NAT-AFFIRMATIVEACTION-02-glhf-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/08/03/us/affirmative-action-military-academies.html",
            date_str="August 2023",
        ),
    ),
    (
        FrontendArticle(
            title="CUNY Chief Gives Tenure To Professor In Brooklyn",
            abstract="City University of New York board overrules Brooklyn College officials and grants tenure to history professor Robert D Johnson; case drew national attention last year when he was denied tenured on ground of being uncollegial (M)",
            img_url=None,
            article_url="https://www.nytimes.com/2003/02/25/nyregion/cuny-chief-gives-tenure-to-professor-in-brooklyn.html",
            date_str="February 2003",
        ),
        FrontendArticle(
            title="Texas A&M Agrees to $1 Million Settlement With Journalism Professor",
            abstract="A university report found that fears of a conservative backlash botched the effort to hire a Black professor, Kathleen McElroy, to run its journalism program.",
            img_url="https://static01.nyt.com/images/2023/08/03/multimedia/03NAT-TEXAS-AM-wqgz/03NAT-TEXAS-AM-wqgz-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/08/03/us/texas-am-mcelroy-settlement.html",
            date_str="August 2023",
        ),
    ),
    (
        FrontendArticle(
            title="Court Allows Universities to Bar Military Recruiters",
            abstract="Universities may bar military recruiters from their campuses without risking the loss of federal money, a federal appeals court in Philadelphia ruled on Monday.",
            img_url=None,
            article_url="None",
            date_str="November 2004",
        ),
        FrontendArticle(
            title="The College Board Says A.P. Psychology Is ‘Effectively Banned’ in Florida",
            abstract="The nonprofit said it would not remove a section on gender and sexual orientation, as Florida had requested, and advised districts not to offer the course.",
            img_url="https://static01.nyt.com/images/2023/08/03/multimedia/03NAT-FLORIDA-01-wlch/03NAT-FLORIDA-01-wlch-superJumbo-v2.jpg",
            article_url="https://www.nytimes.com/2023/08/03/us/florida-ap-psychology-courses.html",
            date_str="August 2023",
        ),
    ),
    (
        FrontendArticle(
            title="Officers Accused of Lying Face Police Trial",
            abstract="Police officials have filed disciplinary charges against two officers who are accused of lying under oath to help a fellow officer, Francis X. Livoti, cover up his role in the 1994 choking death of Anthony Baez.    The charges were based on testimony the officers, Mario Erotokritou and Anthony Farnan, gave as defense witnesses at Mr. Livoti's 1998 federal trial, at which he was convicted of violating Mr. Baez's civil rights.  ",
            img_url=None,
            article_url="https://www.nytimes.com/2001/04/07/nyregion/officers-accused-of-lying-face-police-trial.html",
            date_str="April 2001",
        ),
        FrontendArticle(
            title="6 Ex-Officers Plead Guilty to Civil Rights Charges in Assault on 2 Black Men in Mississippi",
            abstract="The authorities said that the two men had been handcuffed, beaten and shocked with Tasers. One of the men was also shot in the mouth during a “mock execution,” and a sex toy was forced into the other man’s mouth, federal prosecutors said.",
            img_url="https://static01.nyt.com/images/2023/08/03/multimedia/03xp-mississippi-lpzf/03xp-mississippi-lpzf-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/08/03/us/mississippi-officers-charged-civil-rights.html",
            date_str="August 2023",
        ),
    ),
    (
        FrontendArticle(
            title="Police Officer Found Guilty In Videotaped Assault Attempt",
            abstract="Police Officer Charles Dorcent is found guilty of attempted assault of Anthony Carty, but is acquitted of assault in second degree; was videotaped apparently striking Carty, who was in handcuffs after his capture in Brooklyn; Dorcent defense offered testimony that he swung at Carty but hit another officer (M)",
            img_url=None,
            article_url="https://www.nytimes.com/2004/03/11/nyregion/police-officer-found-guilty-in-videotaped-assault-attempt.html",
            date_str="March 2004",
        ),
        FrontendArticle(
            title="Ex-Louisiana Trooper Acquitted of Violating Civil Rights of Black Motorist",
            abstract="The trooper beat Aaron Larry Bowman with a flashlight after a traffic stop in 2019. The case drew outrage after police body-camera footage of the encounter went public.",
            img_url="https://static01.nyt.com/images/2023/08/03/multimedia/03xp-louisiana-jplq/03xp-louisiana-jplq-superJumbo.jpg",
            article_url="https://www.nytimes.com/2023/08/03/us/jacob-brown-louisiana-state-trooper-acquitted.html",
            date_str="August 2023",
        ),
    ),
]


@app.route("/")
def index():
    return render_template("index copy.html", results=results)

app.run(host="0.0.0.0", port=3000, debug=True)
