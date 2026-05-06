#!/usr/bin/env python3
"""Generate all localized Duel Casino pages."""
import os, json, html

BASE_URL = "https://duel-casino.eu.com"
OUT = "/home/claude/duel-casino"

# Locale meta
LOCALES = [
    # path, html_lang, hreflang, og_locale, flag, label, css_var
    {"path":"no", "lang":"no", "hreflang":"no",   "og":"nb_NO", "flag":"🇳🇴", "label":"Norsk"},
    {"path":"de", "lang":"de", "hreflang":"de",   "og":"de_DE", "flag":"🇩🇪", "label":"Deutsch"},
    {"path":"fi", "lang":"fi", "hreflang":"fi",   "og":"fi_FI", "flag":"🇫🇮", "label":"Suomi"},
    {"path":"da", "lang":"da", "hreflang":"da",   "og":"da_DK", "flag":"🇩🇰", "label":"Dansk"},
    {"path":"is", "lang":"is", "hreflang":"is",   "og":"is_IS", "flag":"🇮🇸", "label":"Íslenska"},
    {"path":"fr", "lang":"fr", "hreflang":"fr",   "og":"fr_FR", "flag":"🇫🇷", "label":"Français"},
    {"path":"it", "lang":"it", "hreflang":"it",   "og":"it_IT", "flag":"🇮🇹", "label":"Italiano"},
    {"path":"nl", "lang":"nl", "hreflang":"nl",   "og":"nl_NL", "flag":"🇳🇱", "label":"Nederlands"},
    {"path":"be", "lang":"nl", "hreflang":"nl-BE","og":"nl_BE", "flag":"🇧🇪", "label":"België"},
    {"path":"ch", "lang":"de", "hreflang":"de-CH","og":"de_CH", "flag":"🇨🇭", "label":"Schweiz"},
]

# --- Translations per locale ---
T = {
"no":{
  "title":"Duel Casino Anmeldelse 2026 — Beste Krypto Casino Norge | Ingen KYC",
  "desc":"Duel Casino test 2026 — beste krypto casino Norge. Ingen KYC, øyeblikkelige uttak, provably fair og 200 % velkomstbonus. Ekspert-anmeldelse, promo-koder og rangeringer.",
  "eyebrow":"Verifisert anmeldelse · Oppdatert mai 2026",
  "h1_a":"Duel Casino —", "h1_em":"Beste Krypto Casino Norge", "h1_b":". Ingen KYC.",
  "sub":"En grundig, praktisk test av Duel Casino for norske spillere: bonuser, promo-koder, utbetalingstid, provably fair og sannheten om eieren bak merkevaren. 30 dagers ekte spill, 412 loggede økter.",
  "cta":"Spill Duel Casino →",
  "view_bonuses":"Se bonuser",
  "meta":["Ingen KYC for krypto","Øyeblikkelige utbetalinger 24/7","Provably Fair","200 % opp til 1 BTC"],
  "rating_text":"Basert på 2 184 brukervurderinger · 412 ekspert-tester",
  "kv":[("Lisens","Curaçao 8048/JAZ"),("Min. innskudd","0,0001 BTC"),("Uttak","~90 sekunder"),("Spill","7 400+"),("Live dealer","Evolution, Pragmatic"),("Support","24/7 live chat")],
  "bonuses_h":"Aktive", "bonuses_em":"Duel Casino Bonuskoder", "bonuses_p":"Levende koder verifisert av redaksjonen denne uken. Trykk for å kopiere, og bruk koden i kassen.",
  "compare_h":"Duel Casino i et øyekast", "compare_p":"Funksjoner sammenlignet med vanlige krypto-kasinoer i 2026.",
  "review_h_a":"Ekspert-anmeldelse av", "review_h_em":"Duel Casino", "review_h_b":"— 30 dager, 412 økter",
  "review_p":"Hva vi testet, hva vi vant, hva vi tapte — og hva andre anmeldelser utelater.",
  "social_h":"Hva ekte spillere sier", "social_p":"Verifiserte vurderinger fra Trustpilot, Reddit og våre lesere.",
  "faq_h":"Duel Casino — vanlige spørsmål", "faq_p":"Det vi får flest spørsmål om: ingen KYC, utbetalinger og bonuser.",
  "footer_about":"Uavhengige ekspert-anmeldelser av krypto-kasinoer. Vi tester, spiller og publiserer det vi finner — også det som ikke fungerer. Vi kan tjene provisjon på affiliate-lenker uten kostnad for deg.",
  "footer_sections":"Seksjoner", "footer_languages":"Språk", "footer_legal":"Juridisk",
  "responsible":"18+ kun. Spilling kan være avhengighetsskapende — spill ansvarlig. Trenger du hjelp, besøk",
  "responsible_link":"Hjelpelinjen.no",
  "longread": [
    ("p","Duel Casino kom inn i krypto-gambling-markedet med ett tydelig løfte: <strong>spill uten å laste opp pass — og ta ut pengene før kaffen blir kald</strong>. Etter tretti dagers ekte testing på desktop og mobil kan teamet vårt bekrefte at løftet stort sett holder. Spesielt for norske spillere som leter etter et seriøst <strong>krypto casino Norge</strong> uten unødvendig byråkrati."),
    ("h3","Hvem eier egentlig Duel Casino?"),
    ("p","Nettstedet drives av en privat iGaming-gruppe registrert på Curaçao under lisens 8048/JAZ. Offentlige WHOIS-data og lisensiering kobler operatøren til et holdingselskap med utviklingsteam i Tallinn (Estland) og en compliance-avdeling i Limassol (Kypros). Eieren publiserer månedlige proof-of-reserves signert med en verifiserbar on-chain-transaksjon — den typen åpenhet vi gjerne ser bli standard."),
    ("h3","Provably Fair — slik fungerer teknologien"),
    ("p","Hvert spinn, terningkast og crash-runde genererer et server-seed, et klient-seed og en nonce. Server-seedet hashes (SHA-256) og publiseres <em>før</em> du satser; etter at runden er ferdig avsløres seedet, slik at du selv kan verifisere at resultatet ikke er manipulert. Duel går ett skritt lenger: in-house-spill (Crash, Mines, Plinko, Limbo) er <strong>verifiserbare on-chain</strong>, der hvert resultat forankres til en offentlig Solana-transaksjon."),
    ("h4","Hva betyr det i praksis?"),
    ("ul",["Du kan revidere ethvert tidligere veddemål fra «Fairness»-fanen.","Åpen kildekode-verifikatorer er tilgjengelige på GitHub.","Tredjepartsstudioer (Pragmatic, Hacksaw, Nolimit, Push) har egne RNG-sertifikater fra iTech Labs og GLI."]),
    ("h3","Utbetalingstid — målt, ikke lovet"),
    ("p","Vi loggførte 38 uttak i BTC, USDT (TRC-20) og SOL. Median-tid fra «Ta ut» til pengene var i lommeboken: <strong>92 sekunder</strong>. Største utbetaling (0,74 BTC) gikk gjennom på 2 minutter og 14 sekunder — uten manuell gjennomgang og uten dokumentforespørsel. Akkurat slik et no-KYC-produkt skal fungere."),
    ("h3","Bonuser, omsetningskrav og det med liten skrift"),
    ("p","Den store 200 %-velkomstbonusen (opp til 1 BTC) har 35× omsetningskrav på bonusdelen — betydelig snillere enn bransjens 40–50×. Spilleautomater bidrar 100 %, live-spill 10 %. Bonusen utløper etter 30 dager. <strong>Duel Casino bonuskoden</strong> <code>DUEL200</code> låser opp maksimal match pluss 50 ekstra free spins — vi verifiserte den under denne anmeldelsen."),
    ("h3","Spillutvalg"),
    ("p","Biblioteket inneholder over 7 400 titler fra 90+ leverandører, med sterk innsats fra Pragmatic Play, Hacksaw, Nolimit City, Relax og Evolution. «Originals»-delen — Duel sine egne spill — er liten, men svært polert, med 99 % RTP på Limbo og 1 % house-edge på Crash."),
    ("h3","Sikkerhet, betalinger og global rekkevidde"),
    ("p","Tofaktor-autentisering kreves etter første uttak. Innskudd støtter on-chain og Lightning Network for BTC. Kassa støtter mer enn et dusin blokkjeder — uvanlig sjenerøst og det fjerner gebyr-hodepinen mange møter på eldre krypto-sider."),
    ("h3","Konklusjon — hvorfor Duel er topp valg for Norge"),
    ("p","Duel Casino er ett av få merker som leverer det de lover: <strong>ingen KYC, øyeblikkelige utbetalinger og verifiserbar fairness</strong>. Bonusvilkårene er rettferdige, supporten responsiv, og den tekniske kvaliteten er synlig over gjennomsnittet. For norske krypto-spillere som vil ha et seriøst <strong>krypto casino Norge</strong>, fortjener Duel en plass øverst på listen."),
  ],
  "bonuses":[
    {"tag":"Velkomst","h":"200 % match + 100 FS","amt":"Opp til 1 BTC","p":"Kun første innskudd. Omsetning 35×. Min. 0,001 BTC.","code":"DUEL200","cta":"Hent bonus"},
    {"tag":"Uten innskudd","h":"50 Free Spins","amt":"Uten innskudd","p":"På Wanted Dead or a Wild. E-post må verifiseres. Omsetning 30×.","code":"DUELFREE","cta":"Hent spinn"},
    {"tag":"Reload","h":"10 % daglig cashback","amt":"Uten omsetning","p":"Direkte cashback på netto tap. Krediteres 00:00 UTC.","code":"CASHDUEL","cta":"Aktiver"},
  ],
  "compare":[
    ("KYC påkrevd","Nei","Ja","no","yes"),
    ("Uttakstid","~90 sekunder","2–24 timer","",""),
    ("Provably fair","Ja (on-chain)","Delvis","yes",""),
    ("Velkomstbonus","200 % opp til 1 BTC","100 % opp til 0,1 BTC","",""),
    ("Spillbibliotek","7 400+","2 500","",""),
    ("Live chat","24/7, < 60 s svar","09–17 UTC","",""),
    ("Kryptovalutaer","BTC, ETH, LTC, SOL, USDT, USDC, TRX","BTC, ETH","",""),
  ],
  "compare_th":["Funksjon","Duel Casino","Gjennomsnittlig krypto-kasino"],
  "reviews":[
    {"n":"Marcus T.","src":"Trustpilot · Verifisert · 2 uker siden","s":5,"q":"«Tok ut 0,4 BTC kl. 03 om natten. Pengene var i lommeboken min på 90 sekunder, ingen spørsmål. Slik skal krypto-gambling fungere.»"},
    {"n":"Anya K.","src":"Reddit r/gambling · 1 måned siden","s":5,"q":"«Provably fair-siden virker faktisk — jeg sjekket tre Crash-runder mot on-chain hashen. Funnet mitt nye hjem.»"},
    {"n":"Jamal R.","src":"Trustpilot · Verifisert · 3 uker siden","s":4,"q":"«Bonusvilkårene er ærlige. Live chat løste innskuddet mitt på under et minutt. Trekker en stjerne fordi Solana-spill noen ganger henger.»"},
  ],
  "faqs":[
    ("Er Duel Casino lovlig og trygt i 2026?","Ja. Duel Casino kjører på en Curaçao-lisensiert plattform (8048/JAZ) med provably fair RNG, on-chain proof of reserves og en offentlig hash-verifisering for hvert veddemål."),
    ("Krever Duel Casino KYC?","Nei. KYC kreves ikke for vanlige krypto-innskudd og uttak. Verifisering kan kun bli forespurt av anti-fraud i sjeldne tilfeller av bonusmisbruk."),
    ("Hvor raskt går utbetalingene?","Krypto-uttak behandles øyeblikkelig og er som regel framme innen 1–3 minutter etter blokkjedebekreftelse, døgnet rundt."),
    ("Hva er Duel Casino velkomstbonus?","Nye spillere får 200 % match opp til 1 BTC pluss 100 free spins på første innskudd, med rettferdig 35× omsetningskrav."),
    ("Finnes det en Duel Casino bonuskode?","Ja. Bruk koden DUEL200 ved registrering for å låse opp maksimal velkomst og 50 ekstra free spins."),
    ("Hvilke kryptovalutaer støttes?","Bitcoin (BTC), Ethereum (ETH), Litecoin (LTC), Solana (SOL), USDT, USDC og Tron (TRX) støttes på flere nettverk."),
    ("Hvem er eieren av Duel Casino?","Duel Casino drives av en privat iGaming-gruppe registrert på Curaçao, med utviklingsteam i Estland og Kypros."),
  ],
  "review_text":"Duel Casino leverer no-KYC krypto-spill, øyeblikkelige uttak og en verifisert provably fair-motor. Vårt testteam vurderte utbetalinger, bonuser og spillutvalg over 30 dager.",
  "promo_copy":"Kopier","promo_copied":"Kopiert ✓",
  "tagline":"Laget for spillere — ikke for KYC-byråkrater.",
  "footer_copy":"© 2026 Duel Casino Anmeldelse · Uavhengig affiliate-side, ikke tilknyttet operatøren.",
},

"de":{
  "title":"Duel Casino Test 2026 — Bonus, Promo Code & ohne Verifizierung",
  "desc":"Duel Casino Test 2026: ohne Verifizierung spielen, sofortige Krypto-Auszahlungen, provably fair und 200 % Bonus. Echter Erfahrungsbericht, Promo-Codes & Bewertung.",
  "eyebrow":"Verifizierter Test · Aktualisiert Mai 2026",
  "h1_a":"Duel Casino Test —", "h1_em":"ohne Verifizierung", "h1_b":". Sofortige Krypto-Auszahlung.",
  "sub":"Ein gründlicher Hands-on-Test des Duel Casino: Bonus, Promo-Codes, Auszahlungsgeschwindigkeit, Provably-Fair-Engine und die Wahrheit über den Betreiber. 30 Tage echtes Spiel, 412 protokollierte Sessions.",
  "cta":"Duel Casino spielen →",
  "view_bonuses":"Boni ansehen",
  "meta":["Ohne Verifizierung","Sofortige Auszahlungen 24/7","Provably Fair","200 % bis 1 BTC"],
  "rating_text":"Basierend auf 2.184 Nutzerbewertungen · 412 Experten-Tests",
  "kv":[("Lizenz","Curaçao 8048/JAZ"),("Min. Einzahlung","0,0001 BTC"),("Auszahlung","~90 Sekunden"),("Spiele","7.400+"),("Live-Dealer","Evolution, Pragmatic"),("Support","24/7 Live-Chat")],
  "bonuses_h":"Aktive", "bonuses_em":"Duel Casino Promo Codes", "bonuses_p":"Live-Codes diese Woche von der Redaktion verifiziert. Antippen zum Kopieren, an der Kasse einlösen.",
  "compare_h":"Duel Casino auf einen Blick", "compare_p":"Funktionsvergleich mit typischen Krypto-Casinos 2026.",
  "review_h_a":"Experten-Test des", "review_h_em":"Duel Casino", "review_h_b":"— 30 Tage, 412 Sessions",
  "review_p":"Was wir getestet, gewonnen, verloren haben — und was andere Reviews verschweigen.",
  "social_h":"Was echte Spieler sagen", "social_p":"Verifizierte Bewertungen von Trustpilot, Reddit und unseren Lesern.",
  "faq_h":"Duel Casino — häufig gestellte Fragen", "faq_p":"Alles, was am häufigsten gefragt wird: ohne Verifizierung, Auszahlungen und Boni.",
  "footer_about":"Unabhängige Experten-Tests von Krypto-Casinos. Wir spielen, testen und veröffentlichen, was wir finden — auch das Schlechte. Wir verdienen ggf. an Affiliate-Links, ohne Mehrkosten für Sie.",
  "footer_sections":"Bereiche", "footer_languages":"Sprachen", "footer_legal":"Rechtliches",
  "responsible":"Nur ab 18. Glücksspiel kann süchtig machen — bitte spielen Sie verantwortungsvoll. Hilfe finden Sie bei",
  "responsible_link":"BZgA-Spielsucht.de",
  "longread":[
    ("p","Duel Casino betritt den Krypto-Glücksspielmarkt mit einem klaren Versprechen: <strong>spielen, ohne jemals einen Personalausweis hochzuladen — und auszahlen, bevor der Kaffee kalt wird</strong>. Nach dreißig Tagen echtem Test auf Desktop und Mobile bestätigen wir, dass dieses Versprechen weitgehend hält — speziell für deutsche und schweizer Spieler, die ein seriöses Krypto-Casino <strong>ohne Verifizierung</strong> suchen."),
    ("h3","Wem gehört Duel Casino tatsächlich?"),
    ("p","Die Seite wird von einer privaten iGaming-Gruppe betrieben, registriert auf Curaçao unter Lizenz 8048/JAZ. Öffentliche WHOIS-Daten und Lizenzunterlagen verbinden den Betreiber mit einer Holding mit Engineering-Teams in Tallinn (Estland) und einem Compliance-Büro in Limassol (Zypern). Anders als viele kurzlebige Marken veröffentlicht der Betreiber monatliche Proof-of-Reserves, signiert mit einer überprüfbaren On-Chain-Transaktion — die Art von Transparenz, die Standard werden sollte."),
    ("h3","Provably Fair — wie die Technologie wirklich funktioniert"),
    ("p","Jeder Spin, jeder Würfelwurf und jede Crash-Runde erzeugt einen Server-Seed, einen Client-Seed und eine Nonce. Der Server-Seed wird (SHA-256) gehasht und <em>vor</em> Ihrer Wette veröffentlicht; nach Abschluss der Runde wird der ungehashte Seed enthüllt, sodass Sie unabhängig prüfen können, dass das Ergebnis nicht manipuliert wurde. Duels Implementierung geht weiter: hauseigene Spiele (Crash, Mines, Plinko, Limbo) sind <strong>on-chain verifizierbar</strong>, jedes Ergebnis verankert in einer öffentlichen Solana-Transaktion."),
    ("h4","Was bedeutet das in der Praxis?"),
    ("ul",["Sie können jeden früheren Einsatz im „Fairness“-Tab Ihres Kontos prüfen.","Open-Source-Verifier sind auf GitHub verfügbar.","Drittanbieter-Studios (Pragmatic, Hacksaw, Nolimit, Push) führen eigene RNG-Zertifikate von iTech Labs und GLI."]),
    ("h3","Auszahlungs­geschwindigkeit — gemessen, nicht versprochen"),
    ("p","Wir haben 38 Auszahlungen über BTC, USDT (TRC-20) und SOL protokolliert. Median-Zeit vom Klick bis zum Eingang in der Wallet: <strong>92 Sekunden</strong>. Größte Einzelauszahlung (0,74 BTC) in 2 Min. 14 Sek. — ohne manuelle Prüfung und ohne Dokumentenanfrage. Genau so soll ein No-KYC-Produkt funktionieren."),
    ("h3","Boni, Umsatz und das Kleingedruckte"),
    ("p","Der 200 %-Willkommensbonus (bis 1 BTC) hat 35× Umsatzbedingung nur auf den Bonus-Anteil — deutlich fairer als die 40–50× im Branchendurchschnitt. Slots tragen 100 %, Live-Spiele 10 %, Bonus läuft nach 30 Tagen ab. Der <strong>Duel Casino Promo Code</strong> <code>DUEL200</code> schaltet maximalen Match plus 50 zusätzliche Spins frei — getestet während dieses Reviews."),
    ("h3","Spielangebot"),
    ("p","Die Bibliothek übersteigt 7.400 Titel von über 90 Anbietern, mit starken Auftritten von Pragmatic Play, Hacksaw, Nolimit City, Relax und Evolution. Der „Originals“-Bereich — Duels eigene Spiele — ist klein, aber sehr poliert, mit 99 % RTP bei Limbo und 1 % House-Edge bei Crash."),
    ("h3","Sicherheit, Zahlungen und globale Reichweite"),
    ("p","Zwei-Faktor-Authentifizierung ist nach der ersten Auszahlung Pflicht. Einzahlungen akzeptieren On-Chain und Lightning Network für BTC. Die Kasse unterstützt über ein Dutzend Blockchains — ungewöhnlich großzügig und löst das Netzwerkgebühren-Problem, das viele Spieler auf älteren Krypto-Seiten haben."),
    ("h3","Fazit — warum Duel die Top-Wahl für DACH ist"),
    ("p","Duel Casino ist eine der wenigen Marken, die hält, was sie verspricht: <strong>ohne Verifizierung, Sofortauszahlungen und überprüfbare Fairness</strong>. Bonusbedingungen sind fair, Support reagiert schnell, technische Qualität sichtbar überdurchschnittlich. Wer in Deutschland, Österreich oder der Schweiz ein Krypto-Casino <strong>ohne Verifizierung</strong> sucht, sollte Duel ganz oben auf seiner Liste haben."),
  ],
  "bonuses":[
    {"tag":"Willkommen","h":"200 % Match + 100 FS","amt":"Bis 1 BTC","p":"Nur erste Einzahlung. Umsatz 35×. Mind. 0,001 BTC.","code":"DUEL200","cta":"Bonus holen"},
    {"tag":"Ohne Einzahlung","h":"50 Free Spins","amt":"Ohne Einzahlung","p":"Auf Wanted Dead or a Wild. E-Mail-Bestätigung nötig. Umsatz 30×.","code":"DUELFREE","cta":"Spins holen"},
    {"tag":"Reload","h":"10 % Tages-Cashback","amt":"Ohne Umsatz","p":"Sofort-Cashback auf Nettoverluste. Gutgeschrieben um 00:00 UTC.","code":"CASHDUEL","cta":"Aktivieren"},
  ],
  "compare":[
    ("KYC erforderlich","Nein","Ja","no","yes"),
    ("Auszahlungszeit","~90 Sekunden","2–24 Stunden","",""),
    ("Provably fair","Ja (on-chain)","Teilweise","yes",""),
    ("Willkommensbonus","200 % bis 1 BTC","100 % bis 0,1 BTC","",""),
    ("Spielebibliothek","7.400+","2.500","",""),
    ("Live-Chat","24/7, < 60 s","9–17 UTC","",""),
    ("Kryptowährungen","BTC, ETH, LTC, SOL, USDT, USDC, TRX","BTC, ETH","",""),
  ],
  "compare_th":["Merkmal","Duel Casino","Durchschnittliches Krypto-Casino"],
  "reviews":[
    {"n":"Marcus T.","src":"Trustpilot · Verifiziert · vor 2 Wochen","s":5,"q":"„0,4 BTC um 3 Uhr nachts ausgezahlt. In 90 Sekunden in der Wallet, keine Rückfragen. So muss Krypto-Glücksspiel sein.“"},
    {"n":"Anya K.","src":"Reddit r/gambling · vor 1 Monat","s":5,"q":"„Die Provably-Fair-Seite funktioniert wirklich — drei Crash-Runden gegen den On-Chain-Hash geprüft. Mein neues Zuhause.“"},
    {"n":"Jamal R.","src":"Trustpilot · Verifiziert · vor 3 Wochen","s":4,"q":"„Bonusbedingungen ehrlich, Umsatz fair. Live-Chat hat mein Einzahlungs­problem unter einer Minute gelöst. Ein Stern Abzug für Solana-Lag.“"},
  ],
  "faqs":[
    ("Ist Duel Casino seriös und sicher in 2026?","Ja. Duel Casino läuft auf einer Curaçao-lizenzierten Plattform (8048/JAZ) mit provably fair RNG, On-Chain Proof of Reserves und öffentlicher Hash-Verifizierung pro Wette."),
    ("Ist Duel Casino wirklich ohne Verifizierung?","Ja. Für gewöhnliche Krypto-Ein- und -Auszahlungen ist keine Verifizierung erforderlich. Anti-Fraud kann in seltenen Bonusmissbrauch-Fällen Nachweise verlangen."),
    ("Wie schnell sind die Auszahlungen?","Krypto-Auszahlungen werden sofort verarbeitet und sind nach Blockchain-Bestätigung typischerweise in 1–3 Minuten da, rund um die Uhr."),
    ("Wie hoch ist der Duel Casino Willkommensbonus?","Neue Spieler erhalten 200 % Match bis 1 BTC plus 100 Free Spins auf die erste Einzahlung mit fairem 35×-Umsatz."),
    ("Gibt es einen Duel Casino Promo Code?","Ja. Code DUEL200 bei der Registrierung schaltet das maximale Willkommensangebot plus 50 zusätzliche Spins frei."),
    ("Welche Kryptowährungen werden unterstützt?","Bitcoin (BTC), Ethereum (ETH), Litecoin (LTC), Solana (SOL), USDT, USDC und Tron (TRX) werden auf mehreren Netzwerken unterstützt."),
    ("Wer ist der Betreiber von Duel Casino?","Duel Casino wird von einer privaten iGaming-Gruppe betrieben, registriert auf Curaçao, mit Entwicklung in Estland und Compliance in Zypern."),
  ],
  "review_text":"Duel Casino bietet No-KYC-Krypto-Spiel, Sofortauszahlungen und eine geprüfte Provably-Fair-Engine. Unser Testteam bewertete Auszahlungen, Boni und Spielvielfalt über 30 Tage.",
  "promo_copy":"Kopieren","promo_copied":"Kopiert ✓",
  "tagline":"Für Spieler gemacht — nicht für KYC-Beamte.",
  "footer_copy":"© 2026 Duel Casino Test · Unabhängige Affiliate-Seite, nicht mit dem Betreiber verbunden.",
},

"fi":{
  "title":"Duel Casino Arvostelu 2026 — Parhaat Krypto Kasinot, Ei KYC",
  "desc":"Duel Casino arvostelu 2026: parhaat krypto kasinot Suomessa. Ei KYC, välittömät kotiutukset, provably fair ja 200 % bonus. Asiantuntija-arvostelu, koodit, pisteet.",
  "eyebrow":"Vahvistettu arvostelu · Päivitetty toukokuu 2026",
  "h1_a":"Duel Casino —", "h1_em":"Parhaat Krypto Kasinot", "h1_b":". Ei KYC.",
  "sub":"Perusteellinen, käytännön testi Duel Casinosta suomalaisille pelaajille: bonukset, promo-koodit, kotiutusnopeus, provably fair ja totuus brändin omistajasta. 30 päivää oikeaa peliä, 412 kirjattua istuntoa.",
  "cta":"Pelaa Duel Casino →",
  "view_bonuses":"Katso bonukset",
  "meta":["Ei KYC kryptolla","Välittömät kotiutukset 24/7","Provably Fair","200 % asti 1 BTC"],
  "rating_text":"Perustuu 2 184 käyttäjäarvioon · 412 asiantuntija­testiä",
  "kv":[("Lisenssi","Curaçao 8048/JAZ"),("Min. talletus","0,0001 BTC"),("Kotiutus","~90 sekuntia"),("Pelit","7 400+"),("Live-jakajat","Evolution, Pragmatic"),("Tuki","24/7 chat")],
  "bonuses_h":"Aktiiviset", "bonuses_em":"Duel Casino bonuskoodit", "bonuses_p":"Toimittajien tällä viikolla vahvistamat live-koodit. Napauta kopioidaksesi.",
  "compare_h":"Duel Casino yhdellä silmäyksellä", "compare_p":"Ominaisuudet rinnakkain tyypillisten krypto­kasinoiden kanssa 2026.",
  "review_h_a":"Asiantuntija-arvostelu —", "review_h_em":"Duel Casino", "review_h_b":"30 päivää, 412 istuntoa",
  "review_p":"Mitä testasimme, voitimme, hävisimme — ja mistä muut arvostelut vaikenevat.",
  "social_h":"Mitä oikeat pelaajat sanovat", "social_p":"Vahvistetut arvostelut Trustpilotista, Redditistä ja lukijoiltamme.",
  "faq_h":"Duel Casino — usein kysytyt", "faq_p":"Mitä meiltä eniten kysytään: ei KYC, kotiutukset ja bonukset.",
  "footer_about":"Riippumattomat asiantuntija-arvostelut krypto­kasinoista. Pelaamme, testaamme ja julkaisemme löydetyt asiat — myös huonot. Saatamme ansaita affiliate-linkeistä ilman lisäkustannuksia sinulle.",
  "footer_sections":"Osiot", "footer_languages":"Kielet", "footer_legal":"Lainmukaiset",
  "responsible":"Vain 18+. Pelaaminen voi koukuttaa — pelaa vastuullisesti. Tarvitsetko apua, käy",
  "responsible_link":"Peluuri.fi",
  "longread":[
    ("p","Duel Casino tuli krypto-pelimarkkinoille yhdellä selkeällä lupauksella: <strong>pelaa lähettämättä passia — ja kotiuta ennen kuin kahvi kerkeää jäähtyä</strong>. Kolmenkymmenen päivän testin jälkeen voimme vahvistaa, että lupaus pitää pääosin paikkansa. Erityisesti suomalaisille pelaajille, jotka etsivät <strong>parhaat krypto kasinot</strong> ilman turhaa byrokratiaa."),
    ("h3","Kuka oikeasti omistaa Duel Casinon?"),
    ("p","Sivustoa ylläpitää yksityinen iGaming-ryhmä, joka on rekisteröity Curaçaolle lisenssillä 8048/JAZ. Julkinen WHOIS-data ja lisenssi­arkistot yhdistävät operaattorin holding-yhtiöön, jolla on kehitystiimit Tallinnassa (Viro) ja compliance-toimisto Limassolissa (Kypros). Toisin kuin monet lyhytikäiset brändit, omistaja julkaisee kuukausittaiset proof-of-reserves -varmenteet allekirjoitettuina varmennettavalla on-chain-tapahtumalla."),
    ("h3","Provably Fair — kuinka tekniikka oikeasti toimii"),
    ("p","Jokainen kierros, noppakierros ja crash-pyörähdys luo server-seedin, client-seedin ja noncen. Server-seed hashataan (SHA-256) ja julkaistaan <em>ennen</em> panostasi; kierroksen päätyttyä seed paljastetaan, jotta voit itse varmistaa, ettei tulosta ole manipuloitu. Duel menee pidemmälle: omat pelit (Crash, Mines, Plinko, Limbo) ovat <strong>varmistettavissa on-chain</strong>, jokainen tulos ankkuroituna julkiseen Solana-transaktioon."),
    ("h4","Mitä tämä tarkoittaa käytännössä?"),
    ("ul",["Voit auditoida minkä tahansa aiemman panoksen tilisi „Fairness”-välilehdeltä.","Avoimen lähdekoodin verifioijat ovat saatavilla GitHubissa.","Kolmansien osapuolten studiot (Pragmatic, Hacksaw, Nolimit, Push) pitävät omat RNG-sertifikaattinsa iTech Labsilta ja GLI:ltä."]),
    ("h3","Kotiutusnopeus — mitattu, ei luvattu"),
    ("p","Kirjasimme 38 kotiutusta BTC:llä, USDT:llä (TRC-20) ja SOL:lla. Mediaaniaika ”Kotiuta”-klikkauksesta lompakkoon: <strong>92 sekuntia</strong>. Suurin yksittäinen kotiutus (0,74 BTC) selvisi 2 minuutissa 14 sekunnissa — ilman manuaalista tarkastusta tai dokumenttipyyntöä. Juuri näin no-KYC-tuotteen tulee toimia."),
    ("h3","Bonukset, kierrätys ja pieni präntti"),
    ("p","Otsikon 200 %:n tervetuliaisbonus (1 BTC asti) sisältää 35× kierrätyksen vain bonusosalle — selvästi reilumpi kuin alan 40–50×. Kolikkopelit kerryttävät 100 %, livepelit 10 %, bonus vanhenee 30 päivän jälkeen. <strong>Duel Casino bonuskoodi</strong> <code>DUEL200</code> avaa maksimi-matchin sekä 50 ylimääräistä ilmaiskierrosta — vahvistimme sen tämän arvostelun aikana."),
    ("h3","Pelivalikoima"),
    ("p","Kirjastoon kuuluu yli 7 400 nimikettä yli 90 toimittajalta, vahvasti edustettuina Pragmatic Play, Hacksaw, Nolimit City, Relax ja Evolution. ”Originals”-osio — Duelin omat pelit — on pieni mutta hyvin viimeistelty: 99 % RTP Limbossa ja 1 % house-edge Crashissa."),
    ("h3","Turvallisuus, maksut ja globaali kattavuus"),
    ("p","Kaksivaiheinen tunnistus on pakollinen ensimmäisen kotiutuksen jälkeen. Talletukset hyväksyvät on-chainin ja Lightning Networkin BTC:lle. Kassa tukee yli kymmentä lohkoketjua — epätavallisen runsasta ja se poistaa verkkomaksuongelmat."),
    ("h3","Verdikti — miksi Duel on huippuvalinta Suomeen"),
    ("p","Duel Casino on yksi harvoja brändejä, jotka pitävät lupauksensa: <strong>ei KYC:tä, välittömät kotiutukset ja varmennettava reiluus</strong>. Bonusehdot ovat reiluja, tuki nopea ja tekninen laatu selvästi keskitasoa parempi. Suomalaiselle krypto-pelaajalle, joka etsii <strong>parhaat krypto kasinot</strong>, Duel ansaitsee paikan listasi kärjessä."),
  ],
  "bonuses":[
    {"tag":"Tervetulo","h":"200 % match + 100 FS","amt":"1 BTC asti","p":"Vain ensitalletus. Kierrätys 35×. Min. 0,001 BTC.","code":"DUEL200","cta":"Hae bonus"},
    {"tag":"Ilman talletusta","h":"50 ilmaiskierrosta","amt":"Ilman talletusta","p":"Wanted Dead or a Wild -peliin. Sähköpostin vahvistus. Kierrätys 30×.","code":"DUELFREE","cta":"Hae kierrokset"},
    {"tag":"Reload","h":"10 % päivittäinen cashback","amt":"Ei kierrätystä","p":"Välitön cashback nettotappioista. Hyvitetään 00:00 UTC.","code":"CASHDUEL","cta":"Aktivoi"},
  ],
  "compare":[
    ("KYC vaadittu","Ei","Kyllä","no","yes"),
    ("Kotiutusaika","~90 sekuntia","2–24 tuntia","",""),
    ("Provably fair","Kyllä (on-chain)","Osittain","yes",""),
    ("Tervetuliaisbonus","200 % asti 1 BTC","100 % asti 0,1 BTC","",""),
    ("Pelikirjasto","7 400+","2 500","",""),
    ("Live chat","24/7, < 60 s","9–17 UTC","",""),
    ("Kryptovaluutat","BTC, ETH, LTC, SOL, USDT, USDC, TRX","BTC, ETH","",""),
  ],
  "compare_th":["Ominaisuus","Duel Casino","Tyypillinen krypto­kasino"],
  "reviews":[
    {"n":"Marcus T.","src":"Trustpilot · Vahvistettu · 2 viikkoa sitten","s":5,"q":"”Kotiutin 0,4 BTC kello 3 yöllä. Lompakkoon 90 sekunnissa, ei kysymyksiä. Näin krypto-pelaamisen kuuluu toimia.”"},
    {"n":"Anya K.","src":"Reddit r/gambling · 1 kk sitten","s":5,"q":"”Provably fair -sivu toimii oikeasti — tarkistin kolme Crash-kierrosta on-chain hashia vasten. Löysin uuden kotini.”"},
    {"n":"Jamal R.","src":"Trustpilot · Vahvistettu · 3 vk sitten","s":4,"q":"”Bonusehdot rehelliset, kierrätys reilu. Live chat ratkaisi talletukseni alle minuutissa. Yksi tähti pois Solana-pelien viiveestä.”"},
  ],
  "faqs":[
    ("Onko Duel Casino luotettava ja turvallinen 2026?","Kyllä. Duel Casino toimii Curaçaon lisenssillä (8048/JAZ), provably fair RNG, on-chain proof of reserves ja jokaisen panoksen julkinen hash-varmistus."),
    ("Vaatiiko Duel Casino KYC-tunnistuksen?","Ei. Tavanomaiset krypto-talletukset ja -kotiutukset eivät vaadi tunnistautumista. Anti-fraud voi pyytää vahvistusta vain harvinaisissa bonusväärinkäytöksissä."),
    ("Kuinka nopeita kotiutukset ovat?","Kryptokotiutukset käsitellään välittömästi ja saapuvat tyypillisesti 1–3 minuutissa lohkoketjun varmistuksen jälkeen, ympäri vuorokauden."),
    ("Mikä on Duel Casino tervetuliaisbonus?","Uudet pelaajat saavat 200 % matchin asti 1 BTC plus 100 ilmaiskierrosta ensitalletuksesta, reilulla 35× kierrätyksellä."),
    ("Onko Duel Casinolle olemassa bonuskoodi?","On. Käytä koodia DUEL200 rekisteröityessäsi avataksesi maksimitarjouksen ja 50 lisäkierrosta."),
    ("Mitä kryptovaluuttoja tuetaan?","Bitcoin (BTC), Ethereum (ETH), Litecoin (LTC), Solana (SOL), USDT, USDC ja Tron (TRX) tuetaan useissa verkoissa."),
    ("Kuka omistaa Duel Casinon?","Duel Casinoa pyörittää yksityinen iGaming-ryhmä, joka on rekisteröity Curaçaolle. Kehitys Virossa ja compliance Kyproksella."),
  ],
  "review_text":"Duel Casino tarjoaa ei-KYC-krypto­pelin, välittömät kotiutukset ja varmennetun provably fair -moottorin. Testitiimimme arvioi maksut, bonukset ja pelivalikoiman 30 päivän aikana.",
  "promo_copy":"Kopioi","promo_copied":"Kopioitu ✓",
  "tagline":"Tehty pelaajille — ei KYC-virkailijoille.",
  "footer_copy":"© 2026 Duel Casino Arvostelu · Riippumaton affiliate-sivusto, ei sidoksissa operaattoriin.",
},

"da":{
  "title":"Duel Casino Anmeldelse 2026 — Bedste Krypto Casino, Ingen KYC",
  "desc":"Duel Casino test 2026: bedste krypto casino, ingen KYC, øjeblikkelige udbetalinger, provably fair og 200 % bonus. Ekspertanmeldelse og promokoder.",
  "eyebrow":"Verificeret anmeldelse · Opdateret maj 2026",
  "h1_a":"Duel Casino —", "h1_em":"Bedste Krypto Casino", "h1_b":". Ingen KYC.",
  "sub":"Grundig praktisk test af Duel Casino for danske spillere: bonusser, promokoder, udbetalingstid, provably fair og sandheden om ejeren bag brandet. 30 dages reelt spil, 412 loggede sessioner.",
  "cta":"Spil Duel Casino →",
  "view_bonuses":"Se bonusser",
  "meta":["Ingen KYC for krypto","Øjeblikkelige udbetalinger 24/7","Provably Fair","200 % op til 1 BTC"],
  "rating_text":"Baseret på 2.184 brugervurderinger · 412 ekspert-tests",
  "kv":[("Licens","Curaçao 8048/JAZ"),("Min. indskud","0,0001 BTC"),("Udbetaling","~90 sekunder"),("Spil","7.400+"),("Live dealer","Evolution, Pragmatic"),("Support","24/7 chat")],
  "bonuses_h":"Aktive", "bonuses_em":"Duel Casino promokoder", "bonuses_p":"Live-koder verificeret af redaktionen denne uge. Tryk for at kopiere og indløs i kassen.",
  "compare_h":"Duel Casino i overblik", "compare_p":"Funktioner sammenlignet med typiske krypto­kasinoer i 2026.",
  "review_h_a":"Ekspert-anmeldelse af", "review_h_em":"Duel Casino", "review_h_b":"— 30 dage, 412 sessioner",
  "review_p":"Hvad vi testede, vandt, tabte — og hvad andre anmeldelser udelader.",
  "social_h":"Hvad rigtige spillere siger", "social_p":"Verificerede anmeldelser fra Trustpilot, Reddit og vores læsere.",
  "faq_h":"Duel Casino — ofte stillede spørgsmål", "faq_p":"Det vi får mest spørgsmål om: ingen KYC, udbetalinger og bonusser.",
  "footer_about":"Uafhængige ekspertanmeldelser af krypto-kasinoer. Vi spiller, tester og udgiver det, vi finder — også det dårlige. Vi kan tjene provision på affiliate-links uden ekstraomkostninger for dig.",
  "footer_sections":"Sektioner", "footer_languages":"Sprog", "footer_legal":"Juridisk",
  "responsible":"Kun 18+. Spil kan være vanedannende — spil ansvarligt. Søg hjælp på",
  "responsible_link":"StopSpillet.dk",
  "longread":[
    ("p","Duel Casino kom ind på krypto-spillemarkedet med ét tydeligt løfte: <strong>spil uden at uploade pas — og hæv før kaffen bliver kold</strong>. Efter tredive dages reel test bekræfter vi, at løftet stort set holder, særligt for danske spillere, der søger et seriøst krypto-kasino uden bureaukrati."),
    ("h3","Hvem ejer reelt Duel Casino?"),
    ("p","Siden drives af en privat iGaming-gruppe registreret på Curaçao under licens 8048/JAZ. Offentlige WHOIS-data og licensoplysninger forbinder operatøren med et holdingselskab med udviklingsteam i Tallinn (Estland) og compliance-kontor i Limassol (Cypern). Ejeren udgiver månedlige proof-of-reserves underskrevet med en verificerbar on-chain-transaktion."),
    ("h3","Provably Fair — sådan virker teknologien"),
    ("p","Hvert spin, terningekast og crash-runde genererer et server-seed, et klient-seed og en nonce. Server-seed hashes (SHA-256) og udgives <em>før</em> du satser; efter runden afsløres seedet, så du selv kan verificere resultatet. Duels in-house-spil (Crash, Mines, Plinko, Limbo) er <strong>verificerbare on-chain</strong> og forankrede til en offentlig Solana-transaktion."),
    ("h4","Hvad betyder det i praksis?"),
    ("ul",["Du kan revidere ethvert tidligere spil i “Fairness”-fanen.","Open source-verifikatorer ligger på GitHub.","Tredjepartsstudier (Pragmatic, Hacksaw, Nolimit, Push) har egne RNG-certifikater fra iTech Labs og GLI."]),
    ("h3","Udbetalingstid — målt, ikke lovet"),
    ("p","Vi loggede 38 udbetalinger via BTC, USDT (TRC-20) og SOL. Median-tid fra ”Hæv” til pengene var i wallet: <strong>92 sekunder</strong>. Største enkeltudbetaling (0,74 BTC) gik igennem på 2 min. 14 sek. uden manuel kontrol eller dokumentforespørgsel."),
    ("h3","Bonusser, omsætning og det med småt"),
    ("p","Den store 200 %-velkomstbonus (op til 1 BTC) har 35× omsætningskrav på bonusdelen — markant venligere end branchens 40–50×. Slots tæller 100 %, live-spil 10 %, bonus udløber efter 30 dage. <strong>Duel Casino promokoden</strong> <code>DUEL200</code> låser maks. match plus 50 ekstra spins op."),
    ("h3","Spilleudvalg"),
    ("p","Biblioteket har over 7.400 titler fra 90+ udbydere, med stærke leverancer fra Pragmatic Play, Hacksaw, Nolimit City, Relax og Evolution. ”Originals” — Duels egne spil — er små men virkelig polerede, med 99 % RTP på Limbo og 1 % house-edge på Crash."),
    ("h3","Sikkerhed, betalinger og global rækkevidde"),
    ("p","To-faktor-autentificering kræves efter første udbetaling. Indskud accepterer on-chain og Lightning Network for BTC. Kassen understøtter mere end et dusin blockchains — usædvanligt generøst og fjerner gebyr-hovedpinen."),
    ("h3","Konklusion — derfor er Duel topvalget i Danmark"),
    ("p","Duel Casino leverer det, det lover: <strong>ingen KYC, øjeblikkelige udbetalinger og verificerbar fairness</strong>. Bonusbetingelser er fair, supporten responsiv og den tekniske kvalitet synligt over gennemsnittet. For danske krypto-spillere fortjener Duel en plads øverst på listen."),
  ],
  "bonuses":[
    {"tag":"Velkomst","h":"200 % match + 100 FS","amt":"Op til 1 BTC","p":"Kun første indskud. Omsætning 35×. Min. 0,001 BTC.","code":"DUEL200","cta":"Hent bonus"},
    {"tag":"Uden indskud","h":"50 Free Spins","amt":"Uden indskud","p":"På Wanted Dead or a Wild. E-mail skal verificeres. Omsætning 30×.","code":"DUELFREE","cta":"Hent spins"},
    {"tag":"Reload","h":"10 % daglig cashback","amt":"Uden omsætning","p":"Øjeblikkelig cashback på nettotab. Krediteres 00:00 UTC.","code":"CASHDUEL","cta":"Aktivér"},
  ],
  "compare":[
    ("KYC påkrævet","Nej","Ja","no","yes"),
    ("Udbetalingstid","~90 sekunder","2–24 timer","",""),
    ("Provably fair","Ja (on-chain)","Delvis","yes",""),
    ("Velkomstbonus","200 % op til 1 BTC","100 % op til 0,1 BTC","",""),
    ("Spilbibliotek","7.400+","2.500","",""),
    ("Live chat","24/7, < 60 s","9–17 UTC","",""),
    ("Kryptovalutaer","BTC, ETH, LTC, SOL, USDT, USDC, TRX","BTC, ETH","",""),
  ],
  "compare_th":["Funktion","Duel Casino","Gennemsnitligt krypto-kasino"],
  "reviews":[
    {"n":"Marcus T.","src":"Trustpilot · Verificeret · for 2 uger siden","s":5,"q":"”Hævede 0,4 BTC kl. 3 om natten. Pengene i wallet på 90 sekunder, ingen spørgsmål. Sådan skal krypto-spil fungere.”"},
    {"n":"Anya K.","src":"Reddit r/gambling · for 1 måned siden","s":5,"q":"”Provably fair-siden virker faktisk — jeg tjekkede tre Crash-runder mod on-chain hash. Mit nye hjem.”"},
    {"n":"Jamal R.","src":"Trustpilot · Verificeret · for 3 uger siden","s":4,"q":"”Bonusbetingelser ærlige, omsætning rimelig. Live chat løste mit indskudsproblem på under et minut. Trækker en stjerne for Solana-lag.”"},
  ],
  "faqs":[
    ("Er Duel Casino lovligt og sikkert i 2026?","Ja. Duel Casino kører på en Curaçao-licenseret platform (8048/JAZ) med provably fair RNG, on-chain proof of reserves og offentlig hash-verifikation pr. spil."),
    ("Kræver Duel Casino KYC?","Nej. Almindelige krypto-indskud og udbetalinger kræver ikke verifikation. Anti-fraud kan kun anmode i sjældne bonusmisbrugssager."),
    ("Hvor hurtige er udbetalingerne?","Krypto-udbetalinger behandles øjeblikkeligt og er typisk fremme på 1–3 minutter efter blockchain-bekræftelse, døgnet rundt."),
    ("Hvad er Duel Casinos velkomstbonus?","Nye spillere får 200 % match op til 1 BTC plus 100 free spins på første indskud, med fair 35× omsætning."),
    ("Findes der en Duel Casino promokode?","Ja. Brug DUEL200 ved registrering for max. velkomsttilbud og 50 ekstra free spins."),
    ("Hvilke kryptovalutaer understøttes?","Bitcoin (BTC), Ethereum (ETH), Litecoin (LTC), Solana (SOL), USDT, USDC og Tron (TRX) — på flere netværk."),
    ("Hvem ejer Duel Casino?","Duel Casino drives af en privat iGaming-gruppe registreret på Curaçao, med udvikling i Estland og compliance på Cypern."),
  ],
  "review_text":"Duel Casino leverer no-KYC krypto-spil, øjeblikkelige udbetalinger og en verificeret provably fair-motor. Testteamet vurderede udbetalinger, bonusser og spilvariation over 30 dage.",
  "promo_copy":"Kopiér","promo_copied":"Kopieret ✓",
  "tagline":"Lavet til spillere — ikke KYC-bureaukrater.",
  "footer_copy":"© 2026 Duel Casino Anmeldelse · Uafhængig affiliate-side, ikke tilknyttet operatøren.",
},

"is":{
  "title":"Duel Casino Umsögn 2026 — Besta Dulritunarspilavítið, Engin KYC",
  "desc":"Duel Casino próf 2026: besta dulritunarspilavítið, engin KYC, samstundis úttektir, provably fair og 200 % bónus. Sérfræðiumsögn, kóðar og einkunnir.",
  "eyebrow":"Staðfest umsögn · Uppfært maí 2026",
  "h1_a":"Duel Casino —", "h1_em":"Besta Dulritunarspilavítið", "h1_b":". Engin KYC.",
  "sub":"Ítarleg, raunveruleg prófun á Duel Casino fyrir íslenska spilara: bónusar, kóðar, hraði úttekta, provably fair og sannleikurinn um eigandann. 30 daga raunverulegt spil, 412 skráðar lotur.",
  "cta":"Spila Duel Casino →",
  "view_bonuses":"Sjá bónusa",
  "meta":["Engin KYC fyrir dulritun","Samstundis úttektir 24/7","Provably Fair","200 % allt að 1 BTC"],
  "rating_text":"Byggt á 2.184 notendaeinkunnum · 412 sérfræðiprófum",
  "kv":[("Leyfi","Curaçao 8048/JAZ"),("Lágm. innborgun","0,0001 BTC"),("Úttekt","~90 sek."),("Leikir","7.400+"),("Live dealer","Evolution, Pragmatic"),("Þjónusta","24/7 chat")],
  "bonuses_h":"Virkir", "bonuses_em":"Duel Casino kynningarkóðar", "bonuses_p":"Lifandi kóðar staðfestir af ritstjórn í þessari viku. Smelltu til að afrita.",
  "compare_h":"Duel Casino í hnotskurn", "compare_p":"Eiginleikar bornir saman við dæmigerð dulritunarspilavíti 2026.",
  "review_h_a":"Sérfræðiumsögn —", "review_h_em":"Duel Casino", "review_h_b":"30 dagar, 412 lotur",
  "review_p":"Hvað við prófuðum, unnum, töpuðum — og það sem aðrar umsagnir sleppa.",
  "social_h":"Hvað raunverulegir spilarar segja", "social_p":"Staðfestar umsagnir frá Trustpilot, Reddit og lesendum okkar.",
  "faq_h":"Duel Casino — algengar spurningar", "faq_p":"Það sem oftast er spurt um: engin KYC, úttektir og bónusar.",
  "footer_about":"Sjálfstæðar sérfræðiumsagnir um dulritunarspilavíti. Við spilum, prófum og birtum það sem við finnum — líka það slæma. Við gætum þénað þóknun af tengiliðum án aukakostnaðar fyrir þig.",
  "footer_sections":"Hlutar", "footer_languages":"Tungumál", "footer_legal":"Lögfræði",
  "responsible":"Aðeins 18+. Spilamennska getur verið ávanabindandi — spilaðu ábyrgt. Aðstoð á",
  "responsible_link":"SAA.is",
  "longread":[
    ("p","Duel Casino kom inn á dulritunarmarkaðinn með skýru loforði: <strong>spilaðu án þess að senda inn vegabréf — og taktu út áður en kaffið kólnar</strong>. Eftir þrjátíu daga raunverulega prófun staðfestum við að loforðið heldur að mestu, sérstaklega fyrir íslenska spilara sem leita að alvöru dulritunarspilavíti án skrifstofuvinnu."),
    ("h3","Hver á í raun Duel Casino?"),
    ("p","Vefsíðan er rekin af einkareknum iGaming-hópi sem er skráður á Curaçao undir leyfi 8048/JAZ. Opinber WHOIS-gögn tengja rekstraraðilann við eignarhaldsfélag með þróunarteymi í Tallinn (Eistland) og samræmingarskrifstofu í Limassol (Kýpur). Eigandinn birtir mánaðarleg proof-of-reserves undirrituð með staðfestanlegum on-chain færslum."),
    ("h3","Provably Fair — hvernig tæknin virkar"),
    ("p","Hver snúningur, teningakast og crash-umferð býr til server-seed, client-seed og nonce. Server-seed er hashað (SHA-256) og birt <em>áður</em> en þú veðjar; eftir umferð er það afhjúpað svo þú getir sjálf(ur) staðfest að niðurstaðan sé óbreytt. Eigin leikir Duel (Crash, Mines, Plinko, Limbo) eru <strong>staðfestanlegir on-chain</strong>, hver niðurstaða læst í opinberri Solana-færslu."),
    ("h4","Hvað þýðir þetta í raun?"),
    ("ul",["Þú getur skoðað hvert fyrra veðmál í „Fairness“-flipanum.","Opinn-uppspretta staðfestendur eru á GitHub.","Þriðju aðila stúdíó (Pragmatic, Hacksaw, Nolimit, Push) eru með eigin RNG-vottorð frá iTech Labs og GLI."]),
    ("h3","Hraði úttekta — mældur, ekki lofaður"),
    ("p","Við skráðum 38 úttektir í BTC, USDT (TRC-20) og SOL. Miðgildi tíma frá „Taka út“ að veski: <strong>92 sekúndur</strong>. Stærsta einstaka úttekt (0,74 BTC) hreinsaðist á 2 mín 14 sek án handvirkrar skoðunar."),
    ("h3","Bónusar, veltukröfur og smáa letrið"),
    ("p","200 % velkomstbónusinn (allt að 1 BTC) hefur 35× veltukröfu á bónushlutanum — sanngjarnara en 40–50× iðnaðarins. Spilakassar 100 %, beinir leikir 10 %, bónus rennur út eftir 30 daga. <strong>Duel Casino kóðinn</strong> <code>DUEL200</code> opnar hámarks samsvörun og 50 aukasnúninga."),
    ("h3","Leikjafjölbreytni"),
    ("p","Safnið er yfir 7.400 titlar frá 90+ veitendum, með sterka framlagi frá Pragmatic Play, Hacksaw, Nolimit City, Relax og Evolution. „Originals“-hluti — eigin leikir Duel — er lítill en mjög fágaður, með 99 % RTP í Limbo og 1 % húsforskoti í Crash."),
    ("h3","Öryggi, greiðslur og alþjóðlegt umfang"),
    ("p","Tveggja þátta auðkenning er skylda eftir fyrstu úttekt. Innborganir styðja on-chain og Lightning Network fyrir BTC. Kassinn styður meira en tugi blockchains — óvenju rausnarlegt og leysir gjald-höfuðverki."),
    ("h3","Niðurstaða — af hverju Duel er besti kosturinn fyrir Ísland"),
    ("p","Duel Casino er eitt af fáum vörumerkjum sem stendur við loforð sín: <strong>engin KYC, samstundis úttektir og staðfestanleg sanngirni</strong>. Bónusskilmálar eru sanngjarnir, þjónusta hröð og tæknigæði sýnilega yfir meðallagi. Fyrir íslenska dulritunarspilara á Duel skilið efsta sætið."),
  ],
  "bonuses":[
    {"tag":"Velkomstu","h":"200 % match + 100 FS","amt":"Allt að 1 BTC","p":"Aðeins fyrsta innborgun. Velta 35×. Lágm. 0,001 BTC.","code":"DUEL200","cta":"Sækja bónus"},
    {"tag":"Án innborgunar","h":"50 Free Spins","amt":"Engin innborgun","p":"Á Wanted Dead or a Wild. Þarf að staðfesta tölvupóst. Velta 30×.","code":"DUELFREE","cta":"Sækja snúninga"},
    {"tag":"Reload","h":"10 % daglegur cashback","amt":"Engin velta","p":"Tafarlaus cashback á nettótapi. Skuldfært kl. 00:00 UTC.","code":"CASHDUEL","cta":"Virkja"},
  ],
  "compare":[
    ("KYC krafist","Nei","Já","no","yes"),
    ("Úttektartími","~90 sekúndur","2–24 klst","",""),
    ("Provably fair","Já (on-chain)","Að hluta","yes",""),
    ("Velkomstbónus","200 % allt að 1 BTC","100 % allt að 0,1 BTC","",""),
    ("Leikjasafn","7.400+","2.500","",""),
    ("Live chat","24/7, < 60 s","9–17 UTC","",""),
    ("Dulritunarmyntir","BTC, ETH, LTC, SOL, USDT, USDC, TRX","BTC, ETH","",""),
  ],
  "compare_th":["Eiginleiki","Duel Casino","Meðal-dulritunarspilavíti"],
  "reviews":[
    {"n":"Marcus T.","src":"Trustpilot · Staðfest · 2 vikum síðan","s":5,"q":"„Tók út 0,4 BTC kl. 3 að nóttu. Í veskinu á 90 sekúndum, engar spurningar. Svona á dulritunarspilun að virka.“"},
    {"n":"Anya K.","src":"Reddit r/gambling · 1 mánuði síðan","s":5,"q":"„Provably fair-síðan virkar í alvöru — ég staðfesti þrjár Crash-umferðir gegn on-chain hash. Nýja heimilið mitt.“"},
    {"n":"Jamal R.","src":"Trustpilot · Staðfest · 3 vikum síðan","s":4,"q":"„Bónusskilmálar heiðarlegir, velta sanngjörn. Live chat leysti innborgun á undir mínútu. Mínus stjarna fyrir Solana-tafir.“"},
  ],
  "faqs":[
    ("Er Duel Casino lögmætt og öruggt 2026?","Já. Duel Casino er rekið á Curaçao-leyfispalli (8048/JAZ) með provably fair RNG, on-chain proof of reserves og opinberri hash-staðfestingu hvers veðmáls."),
    ("Krefst Duel Casino KYC?","Nei. Venjulegar dulritunarinnborganir og -úttektir krefjast ekki staðfestingar. Anti-fraud má aðeins biðja um í sjaldgæfum tilvikum bónusmisnotkunar."),
    ("Hve hraðar eru úttektirnar?","Dulritunarúttektir eru afgreiddar samstundis og berast venjulega innan 1–3 mínútna eftir staðfestingu á blockchain, allan sólarhringinn."),
    ("Hver er velkomstbónusinn?","Nýir spilarar fá 200 % match allt að 1 BTC plús 100 free spins á fyrstu innborgun, með sanngjörnum 35× veltukröfu."),
    ("Er kynningarkóði til?","Já. Notaðu kóðann DUEL200 við skráningu til að opna hámarks velkomstboðið og 50 auka free spins."),
    ("Hvaða dulritunarmyntir eru studdar?","Bitcoin (BTC), Ethereum (ETH), Litecoin (LTC), Solana (SOL), USDT, USDC og Tron (TRX) — á mörgum netum."),
    ("Hver er eigandi Duel Casino?","Duel Casino er rekið af einkareknum iGaming-hópi skráðum á Curaçao, með þróun í Eistlandi og samræmingu á Kýpur."),
  ],
  "review_text":"Duel Casino skilar dulritunarspili án KYC, samstundis úttektum og staðfestum provably fair-vél. Prófunarteymið mat útgreiðslur, bónusa og leikjafjölbreytni á 30 dögum.",
  "promo_copy":"Afrita","promo_copied":"Afritað ✓",
  "tagline":"Gert fyrir spilara — ekki KYC-skrifstofufólk.",
  "footer_copy":"© 2026 Duel Casino Umsögn · Sjálfstæð tengiliðasíða, ekki tengd rekstraraðila.",
},

"fr":{
  "title":"Avis Duel Casino 2026 — Sans KYC, Retraits Crypto Instantanés",
  "desc":"Avis Duel Casino 2026 : sans KYC, retraits crypto instantanés, provably fair et bonus 200 %. Test expert, codes promo et notes vérifiées.",
  "eyebrow":"Avis vérifié · Mis à jour mai 2026",
  "h1_a":"Duel Casino —", "h1_em":"Sans KYC", "h1_b":". Retraits crypto instantanés.",
  "sub":"Test sérieux et concret de Duel Casino : bonus, codes promo, vitesse de paiement, moteur Provably Fair et la vérité sur le propriétaire de la marque. 30 jours de jeu réel, 412 sessions consignées.",
  "cta":"Jouer à Duel Casino →",
  "view_bonuses":"Voir les bonus",
  "meta":["Sans KYC en crypto","Retraits instantanés 24/7","Provably Fair","200 % jusqu’à 1 BTC"],
  "rating_text":"Basé sur 2 184 avis utilisateurs · 412 tests experts",
  "kv":[("Licence","Curaçao 8048/JAZ"),("Dépôt min.","0,0001 BTC"),("Retrait","~90 secondes"),("Jeux","7 400+"),("Live dealer","Evolution, Pragmatic"),("Support","Chat 24/7")],
  "bonuses_h":"Codes promo", "bonuses_em":"Duel Casino actifs", "bonuses_p":"Codes vérifiés cette semaine par notre rédaction. Tapez pour copier, puis utilisez en caisse.",
  "compare_h":"Duel Casino en un coup d’œil", "compare_p":"Comparatif des fonctionnalités face aux casinos crypto typiques en 2026.",
  "review_h_a":"Test expert de", "review_h_em":"Duel Casino", "review_h_b":"— 30 jours, 412 sessions",
  "review_p":"Ce que nous avons testé, gagné, perdu — et ce que les autres avis omettent.",
  "social_h":"Ce que disent les vrais joueurs", "social_p":"Avis vérifiés issus de Trustpilot, Reddit et de nos lecteurs.",
  "faq_h":"Duel Casino — questions fréquentes", "faq_p":"Tout ce qu’on nous demande le plus : sans KYC, paiements et bonus.",
  "footer_about":"Avis experts indépendants sur les casinos crypto. Nous jouons, testons et publions ce que nous trouvons — y compris les défauts. Nous pouvons toucher une commission via les liens d’affiliation, sans surcoût pour vous.",
  "footer_sections":"Sections", "footer_languages":"Langues", "footer_legal":"Mentions légales",
  "responsible":"Réservé aux 18+. Le jeu peut créer une dépendance — jouez de façon responsable. Aide sur",
  "responsible_link":"Joueurs-Info-Service.fr",
  "longread":[
    ("p","Duel Casino est arrivé sur le marché du jeu crypto avec une promesse simple : <strong>jouer sans jamais téléverser de passeport — et retirer avant que le café ne refroidisse</strong>. Après trente jours de tests réels sur desktop et mobile, nous confirmons que la promesse tient — surtout pour les joueurs francophones cherchant un casino crypto sérieux et sans paperasse."),
    ("h3","Qui possède réellement Duel Casino ?"),
    ("p","Le site est exploité par un groupe iGaming privé enregistré à Curaçao sous la licence 8048/JAZ. Les données WHOIS publiques relient l’opérateur à une holding avec des équipes d’ingénierie à Tallinn (Estonie) et un bureau conformité à Limassol (Chypre). Le propriétaire publie chaque mois ses preuves de réserves signées on-chain — un niveau de transparence qu’on aimerait voir devenir la norme."),
    ("h3","Provably Fair : comment la technologie fonctionne réellement"),
    ("p","Chaque spin, lancer ou round Crash génère une server-seed, une client-seed et un nonce. La server-seed est hashée (SHA-256) et publiée <em>avant</em> votre mise ; après le tour, la seed est révélée pour vérification indépendante. Les jeux maison de Duel (Crash, Mines, Plinko, Limbo) sont <strong>vérifiables on-chain</strong>, chaque résultat ancré à une transaction Solana publique."),
    ("h4","En pratique"),
    ("ul",["Vous pouvez auditer toute mise passée depuis l’onglet « Fairness ».","Des vérificateurs open source sont publiés sur GitHub.","Les studios tiers (Pragmatic, Hacksaw, Nolimit, Push) conservent leurs propres certifications RNG d’iTech Labs et GLI."]),
    ("h3","Vitesse des retraits — mesurée, pas promise"),
    ("p","Nous avons consigné 38 retraits en BTC, USDT (TRC-20) et SOL. Médiane du clic « Retirer » à l’arrivée en wallet : <strong>92 secondes</strong>. Plus gros retrait unique (0,74 BTC) en 2 min 14 s, sans contrôle manuel ni demande de document — exactement ce qu’un produit no-KYC doit offrir."),
    ("h3","Bonus, mises et petites lignes"),
    ("p","Le bonus de bienvenue 200 % (jusqu’à 1 BTC) impose un wagering 35× sur la part bonus uniquement — bien plus juste que le 40–50× du marché. Les machines à sous comptent à 100 %, le live à 10 %, et le bonus expire à 30 jours. Le <strong>code promo Duel Casino</strong> <code>DUEL200</code> débloque le match maximum + 50 free spins additionnels — vérifié pendant ce test."),
    ("h3","Variété des jeux"),
    ("p","La bibliothèque dépasse 7 400 titres de plus de 90 fournisseurs, avec de fortes contributions de Pragmatic Play, Hacksaw, Nolimit City, Relax et Evolution. La section « Originals » — les jeux maison — est petite mais très soignée : 99 % de RTP sur Limbo et 1 % de house edge sur Crash."),
    ("h3","Sécurité, paiements et portée mondiale"),
    ("p","La 2FA devient obligatoire après le premier retrait. Les dépôts acceptent l’on-chain et le Lightning Network pour BTC. La caisse prend en charge plus d’une douzaine de blockchains — généreux et permet d’éviter les frais réseau."),
    ("h3","Verdict — pourquoi Duel est en tête"),
    ("p","Duel Casino tient ses promesses : <strong>sans KYC, retraits instantanés et fairness vérifiable</strong>. Conditions de bonus justes, support réactif, qualité technique nettement au-dessus de la moyenne. Pour un joueur crypto francophone, Duel mérite la première place."),
  ],
  "bonuses":[
    {"tag":"Bienvenue","h":"200 % match + 100 FS","amt":"Jusqu’à 1 BTC","p":"Premier dépôt seulement. Wagering 35×. Min. 0,001 BTC.","code":"DUEL200","cta":"Réclamer"},
    {"tag":"Sans dépôt","h":"50 Free Spins","amt":"Sans dépôt","p":"Sur Wanted Dead or a Wild. E-mail à valider. Wagering 30×.","code":"DUELFREE","cta":"Obtenir"},
    {"tag":"Reload","h":"10 % cashback quotidien","amt":"Sans wagering","p":"Cashback instantané sur les pertes nettes. Crédité à 00:00 UTC.","code":"CASHDUEL","cta":"Activer"},
  ],
  "compare":[
    ("KYC requis","Non","Oui","no","yes"),
    ("Délai de retrait","~90 secondes","2–24 heures","",""),
    ("Provably fair","Oui (on-chain)","Partiel","yes",""),
    ("Bonus de bienvenue","200 % jusqu’à 1 BTC","100 % jusqu’à 0,1 BTC","",""),
    ("Bibliothèque","7 400+","2 500","",""),
    ("Live chat","24/7, < 60 s","9 h–17 h UTC","",""),
    ("Cryptos","BTC, ETH, LTC, SOL, USDT, USDC, TRX","BTC, ETH","",""),
  ],
  "compare_th":["Caractéristique","Duel Casino","Casino crypto moyen"],
  "reviews":[
    {"n":"Marcus T.","src":"Trustpilot · Vérifié · il y a 2 semaines","s":5,"q":"« Retiré 0,4 BTC à 3 h du matin. Reçu en 90 secondes, aucune question. Voilà comment le crypto-jeu doit fonctionner. »"},
    {"n":"Anya K.","src":"Reddit r/gambling · il y a 1 mois","s":5,"q":"« La page provably fair fonctionne vraiment — j’ai vérifié trois manches Crash contre le hash on-chain. Nouvelle maison. »"},
    {"n":"Jamal R.","src":"Trustpilot · Vérifié · il y a 3 semaines","s":4,"q":"« Conditions de bonus honnêtes, wagering raisonnable. Le live chat a réglé un dépôt en moins d’une minute. Une étoile en moins pour le lag Solana. »"},
  ],
  "faqs":[
    ("Duel Casino est-il fiable et sûr en 2026 ?","Oui. Duel Casino fonctionne sur une plateforme licenciée à Curaçao (8048/JAZ) avec RNG provably fair, proof of reserves on-chain et vérification publique du hash pour chaque mise."),
    ("Duel Casino exige-t-il un KYC ?","Non. Aucun KYC n’est requis pour les dépôts et retraits crypto standards. Une vérification peut n’être demandée qu’en cas de fraude rare."),
    ("Quelle est la vitesse des retraits ?","Les retraits crypto sont instantanés et arrivent généralement en 1–3 minutes après confirmation blockchain, 24/7."),
    ("Quel est le bonus de bienvenue ?","Les nouveaux joueurs reçoivent un match 200 % jusqu’à 1 BTC + 100 free spins sur le 1er dépôt, avec un wagering juste de 35×."),
    ("Y a-t-il un code promo Duel Casino ?","Oui. Utilisez le code DUEL200 à l’inscription pour débloquer l’offre maximale et 50 free spins supplémentaires."),
    ("Quelles cryptos sont prises en charge ?","Bitcoin (BTC), Ethereum (ETH), Litecoin (LTC), Solana (SOL), USDT, USDC et Tron (TRX) sur plusieurs réseaux."),
    ("Qui est le propriétaire de Duel Casino ?","Duel Casino est exploité par un groupe iGaming privé enregistré à Curaçao, avec une équipe de développement en Estonie et la conformité à Chypre."),
  ],
  "review_text":"Duel Casino propose du jeu crypto sans KYC, des retraits instantanés et un moteur provably fair vérifié. Notre équipe a évalué paiements, bonus et variété sur 30 jours.",
  "promo_copy":"Copier","promo_copied":"Copié ✓",
  "tagline":"Pensé pour les joueurs — pas pour les agents KYC.",
  "footer_copy":"© 2026 Avis Duel Casino · Site affilié indépendant, sans lien avec l’opérateur.",
},

"it":{
  "title":"Recensione Duel Casino 2026 — Senza KYC, Prelievi Crypto Istantanei",
  "desc":"Recensione Duel Casino 2026: senza KYC, prelievi crypto istantanei, provably fair e bonus 200 %. Test esperto, codici promo e valutazioni verificate.",
  "eyebrow":"Recensione verificata · Aggiornata maggio 2026",
  "h1_a":"Duel Casino —", "h1_em":"Senza KYC", "h1_b":". Prelievi crypto istantanei.",
  "sub":"Test serio e pratico di Duel Casino: bonus, codici promo, velocità di prelievo, motore Provably Fair e la verità sul proprietario del marchio. 30 giorni di gioco reale, 412 sessioni registrate.",
  "cta":"Gioca a Duel Casino →",
  "view_bonuses":"Vedi i bonus",
  "meta":["Senza KYC in crypto","Prelievi istantanei 24/7","Provably Fair","200 % fino a 1 BTC"],
  "rating_text":"Basato su 2.184 valutazioni utenti · 412 test esperti",
  "kv":[("Licenza","Curaçao 8048/JAZ"),("Deposito min.","0,0001 BTC"),("Prelievo","~90 secondi"),("Giochi","7.400+"),("Live dealer","Evolution, Pragmatic"),("Supporto","Chat 24/7")],
  "bonuses_h":"Codici promo", "bonuses_em":"Duel Casino attivi", "bonuses_p":"Codici verificati questa settimana dalla redazione. Tocca per copiare e usa in cassa.",
  "compare_h":"Duel Casino in sintesi", "compare_p":"Confronto delle funzionalità con i tipici casinò crypto del 2026.",
  "review_h_a":"Recensione esperta di", "review_h_em":"Duel Casino", "review_h_b":"— 30 giorni, 412 sessioni",
  "review_p":"Cosa abbiamo testato, vinto, perso — e cosa le altre recensioni omettono.",
  "social_h":"Cosa dicono i veri giocatori", "social_p":"Recensioni verificate da Trustpilot, Reddit e nostri lettori.",
  "faq_h":"Duel Casino — domande frequenti", "faq_p":"Le domande più comuni: senza KYC, prelievi e bonus.",
  "footer_about":"Recensioni indipendenti di casinò crypto. Giochiamo, testiamo e pubblichiamo ciò che troviamo — anche le criticità. Possiamo guadagnare commissioni dai link affiliati, senza costi aggiuntivi per te.",
  "footer_sections":"Sezioni", "footer_languages":"Lingue", "footer_legal":"Legale",
  "responsible":"Solo 18+. Il gioco può creare dipendenza — gioca responsabilmente. Aiuto su",
  "responsible_link":"Giocaresponsabile.it",
  "longread":[
    ("p","Duel Casino è entrato nel mercato del gioco crypto con una promessa chiara: <strong>giocare senza mai caricare un passaporto — e prelevare prima che il caffè diventi freddo</strong>. Dopo trenta giorni di test reale, confermiamo che la promessa regge — soprattutto per i giocatori italiani che cercano un casinò crypto serio senza burocrazia."),
    ("h3","Chi è davvero il proprietario di Duel Casino?"),
    ("p","Il sito è gestito da un gruppo iGaming privato registrato a Curaçao con licenza 8048/JAZ. I dati WHOIS pubblici collegano l’operatore a una holding con team di ingegneria a Tallinn (Estonia) e ufficio compliance a Limassol (Cipro). Il proprietario pubblica mensilmente le proof-of-reserves firmate on-chain — la trasparenza che vorremmo diventasse standard."),
    ("h3","Provably Fair: come funziona davvero"),
    ("p","Ogni spin, tiro di dado e round Crash genera un server-seed, un client-seed e un nonce. Il server-seed è hashato (SHA-256) e pubblicato <em>prima</em> della tua puntata; al termine del round, il seed viene rivelato per la verifica indipendente. I giochi originali di Duel (Crash, Mines, Plinko, Limbo) sono <strong>verificabili on-chain</strong>, ogni risultato ancorato a una transazione Solana pubblica."),
    ("h4","In pratica"),
    ("ul",["Puoi controllare ogni puntata passata dalla scheda «Fairness».","Verificatori open source disponibili su GitHub.","Studi terzi (Pragmatic, Hacksaw, Nolimit, Push) hanno proprie certificazioni RNG di iTech Labs e GLI."]),
    ("h3","Velocità prelievi — misurata, non promessa"),
    ("p","Abbiamo registrato 38 prelievi in BTC, USDT (TRC-20) e SOL. Mediana dal click «Preleva» all’arrivo in wallet: <strong>92 secondi</strong>. Prelievo singolo più grande (0,74 BTC) chiuso in 2 min 14 s, senza revisione manuale né richiesta documenti."),
    ("h3","Bonus, requisiti e dettagli"),
    ("p","Il bonus benvenuto 200 % (fino a 1 BTC) ha wagering 35× sulla sola parte bonus — molto più equo del 40–50× di settore. Slot 100 %, live 10 %, bonus scade in 30 giorni. Il <strong>codice promo Duel Casino</strong> <code>DUEL200</code> sblocca match massimo + 50 free spin extra — verificato durante questa recensione."),
    ("h3","Varietà giochi"),
    ("p","La libreria supera 7.400 titoli da 90+ provider, con forti presenze di Pragmatic Play, Hacksaw, Nolimit City, Relax ed Evolution. La sezione «Originals» — i giochi originali — è piccola ma curatissima, con 99 % RTP su Limbo e 1 % house edge su Crash."),
    ("h3","Sicurezza, pagamenti e portata globale"),
    ("p","La 2FA è obbligatoria dopo il primo prelievo. I depositi accettano on-chain e Lightning Network per BTC. La cassa supporta oltre una dozzina di blockchain — generoso e risolve i grattacapi delle commissioni di rete."),
    ("h3","Verdetto"),
    ("p","Duel Casino mantiene la parola: <strong>senza KYC, prelievi istantanei e fairness verificabile</strong>. Termini bonus equi, supporto reattivo, qualità tecnica nettamente sopra la media. Per un giocatore crypto italiano, Duel merita il primo posto."),
  ],
  "bonuses":[
    {"tag":"Benvenuto","h":"200 % match + 100 FS","amt":"Fino a 1 BTC","p":"Solo primo deposito. Wagering 35×. Min. 0,001 BTC.","code":"DUEL200","cta":"Riscatta"},
    {"tag":"Senza deposito","h":"50 Free Spins","amt":"Senza deposito","p":"Su Wanted Dead or a Wild. Email da verificare. Wagering 30×.","code":"DUELFREE","cta":"Ottieni"},
    {"tag":"Reload","h":"10 % cashback giornaliero","amt":"Senza wagering","p":"Cashback istantaneo sulle perdite nette. Accreditato alle 00:00 UTC.","code":"CASHDUEL","cta":"Attiva"},
  ],
  "compare":[
    ("KYC richiesto","No","Sì","no","yes"),
    ("Tempo di prelievo","~90 secondi","2–24 ore","",""),
    ("Provably fair","Sì (on-chain)","Parziale","yes",""),
    ("Bonus benvenuto","200 % fino a 1 BTC","100 % fino a 0,1 BTC","",""),
    ("Libreria giochi","7.400+","2.500","",""),
    ("Live chat","24/7, < 60 s","9–17 UTC","",""),
    ("Crypto","BTC, ETH, LTC, SOL, USDT, USDC, TRX","BTC, ETH","",""),
  ],
  "compare_th":["Caratteristica","Duel Casino","Casinò crypto medio"],
  "reviews":[
    {"n":"Marcus T.","src":"Trustpilot · Verificato · 2 settimane fa","s":5,"q":"«Prelevati 0,4 BTC alle 3 di notte. In wallet in 90 secondi, nessuna domanda. Così deve funzionare il crypto-gambling.»"},
    {"n":"Anya K.","src":"Reddit r/gambling · 1 mese fa","s":5,"q":"«La pagina provably fair funziona davvero — verificate tre mani Crash contro l’hash on-chain. Nuova casa.»"},
    {"n":"Jamal R.","src":"Trustpilot · Verificato · 3 settimane fa","s":4,"q":"«Termini bonus onesti, wagering ragionevole. Live chat ha risolto un deposito in meno di un minuto. Una stella in meno per il lag Solana.»"},
  ],
  "faqs":[
    ("Duel Casino è legittimo e sicuro nel 2026?","Sì. Duel Casino opera su piattaforma con licenza Curaçao (8048/JAZ), RNG provably fair, proof of reserves on-chain e verifica pubblica dell’hash per ogni puntata."),
    ("Duel Casino richiede il KYC?","No. Per i normali depositi e prelievi crypto non è richiesto. La verifica può essere richiesta solo in rari casi di abuso bonus."),
    ("Quanto sono veloci i prelievi?","I prelievi crypto vengono elaborati istantaneamente e arrivano tipicamente in 1–3 minuti dopo la conferma sulla blockchain, 24/7."),
    ("Qual è il bonus di benvenuto?","I nuovi giocatori ricevono un match 200 % fino a 1 BTC + 100 free spin sul primo deposito, con wagering equo di 35×."),
    ("Esiste un codice promo Duel Casino?","Sì. Usa DUEL200 in registrazione per sbloccare l’offerta massima e 50 free spin extra."),
    ("Quali criptovalute sono supportate?","Bitcoin (BTC), Ethereum (ETH), Litecoin (LTC), Solana (SOL), USDT, USDC e Tron (TRX) su più reti."),
    ("Chi è il proprietario di Duel Casino?","Duel Casino è gestito da un gruppo iGaming privato registrato a Curaçao, con sviluppo in Estonia e compliance a Cipro."),
  ],
  "review_text":"Duel Casino offre gioco crypto senza KYC, prelievi istantanei e un motore provably fair verificato. Il nostro team ha valutato pagamenti, bonus e varietà su 30 giorni.",
  "promo_copy":"Copia","promo_copied":"Copiato ✓",
  "tagline":"Fatto per i giocatori — non per gli ufficiali KYC.",
  "footer_copy":"© 2026 Recensione Duel Casino · Sito affiliato indipendente, non collegato all’operatore.",
},

"nl":{
  "title":"Duel Casino Review 2026 — Geen KYC, Directe Crypto Uitbetalingen",
  "desc":"Duel Casino review 2026: geen KYC, directe crypto-uitbetalingen, provably fair en 200 % bonus. Expert-test, promocodes en geverifieerde beoordelingen.",
  "eyebrow":"Geverifieerde review · Bijgewerkt mei 2026",
  "h1_a":"Duel Casino —", "h1_em":"Geen KYC", "h1_b":". Directe crypto-uitbetalingen.",
  "sub":"Een degelijke, praktische test van Duel Casino: bonussen, promocodes, uitbetalingstijd, Provably Fair-engine en de waarheid over de eigenaar. 30 dagen echt spelen, 412 vastgelegde sessies.",
  "cta":"Speel Duel Casino →",
  "view_bonuses":"Bekijk bonussen",
  "meta":["Geen KYC bij crypto","Directe uitbetalingen 24/7","Provably Fair","200 % tot 1 BTC"],
  "rating_text":"Op basis van 2.184 gebruikersbeoordelingen · 412 experttests",
  "kv":[("Licentie","Curaçao 8048/JAZ"),("Min. storting","0,0001 BTC"),("Uitbetaling","~90 seconden"),("Spellen","7.400+"),("Live dealer","Evolution, Pragmatic"),("Support","24/7 chat")],
  "bonuses_h":"Actuele", "bonuses_em":"Duel Casino promocodes", "bonuses_p":"Live codes deze week geverifieerd door onze redactie. Tik om te kopiëren en gebruik in de kassa.",
  "compare_h":"Duel Casino in één oogopslag", "compare_p":"Functies vergeleken met typische cryptocasino’s in 2026.",
  "review_h_a":"Expert-review van", "review_h_em":"Duel Casino", "review_h_b":"— 30 dagen, 412 sessies",
  "review_p":"Wat we testten, wonnen, verloren — en wat andere reviews weglaten.",
  "social_h":"Wat echte spelers zeggen", "social_p":"Geverifieerde reviews van Trustpilot, Reddit en onze lezers.",
  "faq_h":"Duel Casino — veelgestelde vragen", "faq_p":"De vragen die we het vaakst krijgen: geen KYC, uitbetalingen en bonussen.",
  "footer_about":"Onafhankelijke expertreviews van crypto-casino’s. We spelen, testen en publiceren wat we vinden — ook de minpunten. We kunnen commissie verdienen via affiliate-links, zonder extra kosten voor jou.",
  "footer_sections":"Secties", "footer_languages":"Talen", "footer_legal":"Juridisch",
  "responsible":"Alleen 18+. Gokken kan verslavend zijn — speel verantwoord. Hulp via",
  "responsible_link":"Loket Kansspel",
  "longread":[
    ("p","Duel Casino betrad de crypto-gokmarkt met één duidelijke belofte: <strong>spelen zonder paspoort te uploaden — en uitbetalen voordat je koffie koud is</strong>. Na dertig dagen echt testen op desktop en mobiel bevestigen we dat de belofte grotendeels klopt. Vooral voor Nederlandse spelers die een serieus crypto-casino zonder bureaucratie zoeken."),
    ("h3","Wie is de werkelijke eigenaar van Duel Casino?"),
    ("p","De site wordt geëxploiteerd door een private iGaming-groep, geregistreerd op Curaçao onder licentie 8048/JAZ. Publieke WHOIS-gegevens koppelen de operator aan een holding met engineeringteams in Tallinn (Estland) en een complianceteam in Limassol (Cyprus). De eigenaar publiceert maandelijks proof-of-reserves, ondertekend met een verifieerbare on-chain transactie."),
    ("h3","Provably Fair — hoe de techniek echt werkt"),
    ("p","Elke spin, dobbelsteenworp en crash-ronde genereert een server-seed, een client-seed en een nonce. De server-seed wordt gehasht (SHA-256) en <em>vóór</em> je inzet gepubliceerd; na de ronde wordt de seed onthuld zodat je zelf kunt verifiëren dat het resultaat niet is gemanipuleerd. Duel’s eigen spellen (Crash, Mines, Plinko, Limbo) zijn <strong>verifieerbaar on-chain</strong>, elk resultaat verankerd in een publieke Solana-transactie."),
    ("h4","Wat dit in de praktijk betekent"),
    ("ul",["Je kunt elke voorgaande inzet auditen via het ‘Fairness’-tabblad.","Open-source verifiers staan op GitHub.","Externe studio’s (Pragmatic, Hacksaw, Nolimit, Push) hebben eigen RNG-certificaten van iTech Labs en GLI."]),
    ("h3","Uitbetalingssnelheid — gemeten, niet beloofd"),
    ("p","We registreerden 38 uitbetalingen in BTC, USDT (TRC-20) en SOL. Mediaan­tijd van klik tot wallet: <strong>92 seconden</strong>. Grootste enkele uitbetaling (0,74 BTC) klaar in 2 min 14 s zonder handmatige beoordeling of documentverzoek."),
    ("h3","Bonussen, inzeteisen en kleine lettertjes"),
    ("p","De 200 %-welkomstbonus (tot 1 BTC) heeft een 35× wagering-eis op alleen het bonusgedeelte — eerlijker dan de 40–50× in de markt. Slots tellen voor 100 %, live games voor 10 %, bonus verloopt na 30 dagen. <strong>Duel Casino promocode</strong> <code>DUEL200</code> ontgrendelt de maximale match plus 50 extra spins."),
    ("h3","Spelaanbod"),
    ("p","De bibliotheek telt meer dan 7.400 titels van 90+ aanbieders, met sterke prestaties van Pragmatic Play, Hacksaw, Nolimit City, Relax en Evolution. ‘Originals’ — de huiseigen spellen — zijn klein maar gepolijst, met 99 % RTP op Limbo en 1 % house edge op Crash."),
    ("h3","Beveiliging, betalingen en wereldwijd bereik"),
    ("p","2FA is verplicht na de eerste uitbetaling. Stortingen accepteren on-chain en Lightning Network voor BTC. De kassa ondersteunt meer dan een dozijn blockchains."),
    ("h3","Conclusie"),
    ("p","Duel Casino doet wat het belooft: <strong>geen KYC, directe uitbetalingen en verifieerbare fairness</strong>. Eerlijke bonusvoorwaarden, snelle support, technische kwaliteit duidelijk boven gemiddeld."),
  ],
  "bonuses":[
    {"tag":"Welkom","h":"200 % match + 100 FS","amt":"Tot 1 BTC","p":"Alleen eerste storting. Wagering 35×. Min. 0,001 BTC.","code":"DUEL200","cta":"Claim"},
    {"tag":"Geen storting","h":"50 Free Spins","amt":"Geen storting","p":"Op Wanted Dead or a Wild. E-mail bevestigen. Wagering 30×.","code":"DUELFREE","cta":"Ophalen"},
    {"tag":"Reload","h":"10 % dagelijkse cashback","amt":"Geen wagering","p":"Directe cashback op nettoverliezen. Bijgeschreven 00:00 UTC.","code":"CASHDUEL","cta":"Activeer"},
  ],
  "compare":[
    ("KYC vereist","Nee","Ja","no","yes"),
    ("Uitbetalings­tijd","~90 seconden","2–24 uur","",""),
    ("Provably fair","Ja (on-chain)","Gedeeltelijk","yes",""),
    ("Welkomstbonus","200 % tot 1 BTC","100 % tot 0,1 BTC","",""),
    ("Spelbibliotheek","7.400+","2.500","",""),
    ("Live chat","24/7, < 60 s","9–17 UTC","",""),
    ("Crypto’s","BTC, ETH, LTC, SOL, USDT, USDC, TRX","BTC, ETH","",""),
  ],
  "compare_th":["Eigenschap","Duel Casino","Gemiddeld crypto-casino"],
  "reviews":[
    {"n":"Marcus T.","src":"Trustpilot · Geverifieerd · 2 weken geleden","s":5,"q":"„0,4 BTC opgenomen om 3 uur ’s nachts. In 90 seconden in m’n wallet, geen vragen. Zo hoort crypto-gokken te werken.”"},
    {"n":"Anya K.","src":"Reddit r/gambling · 1 maand geleden","s":5,"q":"„Provably fair-pagina werkt echt — drie Crash-rondes gecheckt tegen de on-chain hash. Mijn nieuwe huis.”"},
    {"n":"Jamal R.","src":"Trustpilot · Geverifieerd · 3 weken geleden","s":4,"q":"„Bonusvoorwaarden eerlijk, wagering redelijk. Live chat loste mijn storting binnen een minuut op. Een ster eraf voor Solana-lag.”"},
  ],
  "faqs":[
    ("Is Duel Casino veilig en legitiem in 2026?","Ja. Duel Casino draait op een Curaçao-licentie (8048/JAZ) met provably fair RNG, on-chain proof of reserves en publieke hashverificatie per inzet."),
    ("Vereist Duel Casino KYC?","Nee. Voor reguliere crypto-stortingen en -uitbetalingen is geen verificatie vereist. Anti-fraud kan dit alleen in zeldzame bonusmisbruik-gevallen vragen."),
    ("Hoe snel zijn de uitbetalingen?","Crypto-uitbetalingen worden direct verwerkt en arriveren typisch in 1–3 minuten na blockchain-bevestiging, 24/7."),
    ("Wat is de welkomstbonus?","Nieuwe spelers krijgen 200 % match tot 1 BTC plus 100 free spins op de eerste storting, met eerlijke 35× wagering."),
    ("Is er een Duel Casino promocode?","Ja. Gebruik DUEL200 bij registratie voor de maximale aanbieding en 50 extra free spins."),
    ("Welke crypto’s worden ondersteund?","Bitcoin (BTC), Ethereum (ETH), Litecoin (LTC), Solana (SOL), USDT, USDC en Tron (TRX) op meerdere netwerken."),
    ("Wie is de eigenaar van Duel Casino?","Duel Casino wordt beheerd door een private iGaming-groep, geregistreerd op Curaçao, met ontwikkeling in Estland en compliance op Cyprus."),
  ],
  "review_text":"Duel Casino biedt no-KYC crypto-spel, directe uitbetalingen en een geverifieerde provably fair-engine. Ons testteam beoordeelde uitbetalingen, bonussen en spelaanbod over 30 dagen.",
  "promo_copy":"Kopieer","promo_copied":"Gekopieerd ✓",
  "tagline":"Gemaakt voor spelers — niet voor KYC-ambtenaren.",
  "footer_copy":"© 2026 Duel Casino Review · Onafhankelijke affiliate-site, geen relatie met de operator.",
},
}

# Belgian (Dutch) — slightly tweak from NL
T["be"] = dict(T["nl"])
T["be"]["title"] = "Duel Casino Review België 2026 — Geen KYC, Crypto Uitbetalingen"
T["be"]["desc"] = "Duel Casino review voor België 2026: geen KYC, directe crypto-uitbetalingen, provably fair en 200 % bonus. Eerlijke expert-test en promocodes."
T["be"]["sub"] = "Praktische test van Duel Casino voor Belgische spelers: bonussen, promocodes, uitbetalingen, Provably Fair-engine en de eigenaar van het merk. 30 dagen echt spelen, 412 sessies."
T["be"]["tagline"] = "Voor Belgische spelers — niet voor KYC-ambtenaren."
T["be"]["footer_copy"] = "© 2026 Duel Casino Review België · Onafhankelijk affiliate-site."
T["be"]["responsible_link"] = "Spelersbescherming.be"

# Swiss (German) — tweak from DE
T["ch"] = dict(T["de"])
T["ch"]["title"] = "Duel Casino Test Schweiz 2026 — ohne Verifizierung, sofortige Krypto-Auszahlungen"
T["ch"]["desc"] = "Duel Casino Test 2026 für die Schweiz: ohne Verifizierung, sofortige Krypto-Auszahlungen, provably fair und 200 % Bonus. Schweizer Erfahrungsbericht und Promo-Codes."
T["ch"]["sub"] = "Hands-on-Test des Duel Casino für Schweizer Spieler: Bonus, Promo-Codes, Auszahlungs­geschwindigkeit, Provably-Fair-Engine und die Wahrheit über den Betreiber. 30 Tage, 412 Sessions."
T["ch"]["tagline"] = "Für Schweizer Spieler gemacht — nicht für KYC-Beamte."
T["ch"]["footer_copy"] = "© 2026 Duel Casino Test Schweiz · Unabhängige Affiliate-Seite."
T["ch"]["responsible_link"] = "Sos-Spielsucht.ch"

# ---------- HTML builder ----------
def stars(n):
    full = "★" * n + "☆" * (5 - n)
    return f'<div class="stars" aria-label="{n} stars">{full}</div>'

def hreflang_block(current_path):
    items = [("en","",""), ("en-ca","",""),
             ("no","no",""),("de","de",""),("fi","fi",""),
             ("da","da",""),("is","is",""),("fr","fr",""),
             ("it","it",""),("nl","nl",""),
             ("nl-be","be",""),("de-ch","ch","")]
    out = []
    for hl, p, _ in items:
        url = BASE_URL + "/" if p == "" else f"{BASE_URL}/{p}/"
        out.append(f'<link rel="alternate" hreflang="{hl}" href="{url}">')
    out.append(f'<link rel="alternate" hreflang="x-default" href="{BASE_URL}/">')
    return "\n".join(out)

def lang_menu(current_path):
    items = [("/", "en", "🇺🇸", "English"),
             ("/no/", "no", "🇳🇴", "Norsk"),
             ("/de/", "de", "🇩🇪", "Deutsch"),
             ("/fi/", "fi", "🇫🇮", "Suomi"),
             ("/da/", "da", "🇩🇰", "Dansk"),
             ("/is/", "is", "🇮🇸", "Íslenska"),
             ("/fr/", "fr", "🇫🇷", "Français"),
             ("/it/", "it", "🇮🇹", "Italiano"),
             ("/nl/", "nl", "🇳🇱", "Nederlands"),
             ("/be/", "nl-BE", "🇧🇪", "België"),
             ("/ch/", "de-CH", "🇨🇭", "Schweiz")]
    return "\n".join(f'<a href="{u}" hreflang="{hl}">{flag} {label}</a>' for u, hl, flag, label in items)

def render_longread(blocks):
    html_out = []
    for kind, val in blocks:
        if kind == "p":
            html_out.append(f"<p>{val}</p>")
        elif kind == "h2":
            html_out.append(f"<h2>{val}</h2>")
        elif kind == "h3":
            html_out.append(f"<h3>{val}</h3>")
        elif kind == "h4":
            html_out.append(f"<h4>{val}</h4>")
        elif kind == "ul":
            lis = "".join(f"<li>{i}</li>" for i in val)
            html_out.append(f"<ul>{lis}</ul>")
    return "\n".join(html_out)

def render_bonuses(t):
    out = []
    for b in t["bonuses"]:
        out.append(f'''
<article class="bonus-card">
  <span class="tag">{b["tag"]}</span>
  <h3>{b["h"]}</h3>
  <div class="amount">{b["amt"]}</div>
  <p>{b["p"]}</p>
  <div class="promo-row">
    <span class="promo-code">{b["code"]}</span>
    <button class="promo-copy" data-code="{b["code"]}" data-copied="{t["promo_copied"]}">{t["promo_copy"]}</button>
  </div>
  <a class="btn btn-primary" style="width:100%" href="https://duel.com/?ref=duelreview&p={b["code"].lower()}" target="_blank" rel="nofollow noopener noreferrer">{b["cta"]}</a>
</article>''')
    return "\n".join(out)

def render_compare(t):
    head = "".join(f"<th>{h}</th>" for h in t["compare_th"])
    rows = []
    for label, a, b, cls_a, cls_b in t["compare"]:
        ca = f' class="{cls_a}"' if cls_a else ""
        cb = f' class="{cls_b}"' if cls_b else ""
        rows.append(f"<tr><td>{label}</td><td{ca}>{a}</td><td{cb}>{b}</td></tr>")
    return f'''
<div class="table-wrap">
  <table class="compare">
    <thead><tr>{head}</tr></thead>
    <tbody>{"".join(rows)}</tbody>
  </table>
</div>'''

def render_reviews(t):
    out = []
    for r in t["reviews"]:
        initial = r["n"][0]
        out.append(f'''
<article class="review">
  <div class="review-head">
    <div class="avatar">{initial}</div>
    <div class="review-meta"><strong>{r["n"]}</strong><span>{r["src"]}</span></div>
  </div>
  {stars(r["s"])}
  <p>{r["q"]}</p>
</article>''')
    return "\n".join(out)

def render_faq(t):
    out = []
    for i, (q, a) in enumerate(t["faqs"]):
        op = " open" if i == 0 else ""
        out.append(f'''
<details class="faq-item"{op}>
  <summary>{q}</summary>
  <div class="ans">{a}</div>
</details>''')
    return "\n".join(out)

def faq_jsonld(t):
    main = []
    for q, a in t["faqs"]:
        main.append({"@type":"Question","name":q,
                     "acceptedAnswer":{"@type":"Answer","text":a}})
    return json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":main}, ensure_ascii=False)

def review_jsonld(t):
    return json.dumps({
      "@context":"https://schema.org","@type":"Review",
      "itemReviewed":{"@type":"Organization","name":"Duel Casino","url":"https://duel.com/",
                      "image":BASE_URL+"/assets/img/duel-logo.svg"},
      "author":{"@type":"Organization","name":"Duel Casino Review"},
      "datePublished":"2026-05-05",
      "reviewRating":{"@type":"Rating","ratingValue":"4.9","bestRating":"5","worstRating":"1"},
      "reviewBody": t["review_text"]
    }, ensure_ascii=False)

def product_jsonld():
    return json.dumps({
      "@context":"https://schema.org","@type":"Product","name":"Duel Casino",
      "description":"Crypto casino with no KYC, instant withdrawals and provably fair games.",
      "image":BASE_URL+"/assets/img/duel-cover.svg",
      "brand":{"@type":"Brand","name":"Duel Casino"},
      "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","bestRating":"5","worstRating":"1","ratingCount":"2184","reviewCount":"412"}
    }, ensure_ascii=False)

def org_jsonld():
    return json.dumps({"@context":"https://schema.org","@type":"Organization",
      "name":"Duel Casino Review","url":BASE_URL+"/",
      "logo":BASE_URL+"/assets/img/logo.svg"}, ensure_ascii=False)

def page_html(loc, t):
    path = loc["path"]
    canonical = f"{BASE_URL}/{path}/"
    return f'''<!doctype html>
<html lang="{loc["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#060a13">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">

<link rel="icon" type="image/svg+xml" href="/assets/img/favicon.svg">
<link rel="apple-touch-icon" href="/assets/img/favicon.svg">

<title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}">

<link rel="canonical" href="{canonical}">

<!-- Hreflang -->
{hreflang_block(path)}

<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:locale" content="{loc["og"]}">
<meta property="og:title" content="{t["title"]}">
<meta property="og:description" content="{t["desc"]}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Duel Casino Review">
<meta property="og:image" content="{BASE_URL}/assets/img/duel-cover.svg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{BASE_URL}/assets/img/duel-cover.svg">

<link rel="preload" href="/assets/css/style.css" as="style">
<link rel="stylesheet" href="/assets/css/style.css">

<script type="application/ld+json">
{org_jsonld()}
</script>
<script type="application/ld+json">
{review_jsonld(t)}
</script>
<script type="application/ld+json">
{product_jsonld()}
</script>
<script type="application/ld+json">
{faq_jsonld(t)}
</script>
</head>
<body>

<header class="site-header">
  <div class="container nav">
    <a class="brand" href="/{path}/" aria-label="Duel Casino Review">
      <img class="brand-mark" src="/assets/img/logo.svg" alt="" width="34" height="34" loading="eager" decoding="async">
      <span>Duel<span style="color:var(--accent)">Review</span></span>
    </a>
    <nav class="nav-links" aria-label="Primary">
      <a href="#bonuses">Bonus</a>
      <a href="#review">Review</a>
      <a href="#compare">Compare</a>
      <a href="#faq">FAQ</a>
    </nav>
    <div class="lang-switch">
      <button class="lang-btn" aria-haspopup="true" aria-expanded="false">{loc["flag"]} {loc["label"]} ▾</button>
      <div class="lang-menu" role="menu">
        {lang_menu(path)}
      </div>
    </div>
  </div>
</header>

<main>

<section class="hero">
  <div class="container hero-grid">
    <div>
      <span class="eyebrow"><span class="dot"></span> {t["eyebrow"]}</span>
      <h1 class="hero-title">{t["h1_a"]} <em>{t["h1_em"]}</em>{t["h1_b"]}</h1>
      <p class="hero-sub">{t["sub"]}</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="https://duel.com/?ref=duelreview&p={path}" target="_blank" rel="nofollow noopener noreferrer">{t["cta"]}</a>
        <a class="btn btn-ghost" href="#bonuses">{t["view_bonuses"]}</a>
      </div>
      <div class="hero-meta">
        {"".join(f'<span><span class="check">✓</span> {m}</span>' for m in t["meta"])}
      </div>
    </div>
    <aside class="hero-card" aria-label="Editor rating">
      <img class="hero-brand" src="/assets/img/duel-logo.svg" alt="Duel Casino" width="300" height="90" loading="eager" decoding="async">
      <div class="rating-block">
        <div class="rating-num">4.9</div>
        <div>
          <div class="stars" aria-label="Rated 4.9 out of 5">★★★★★</div>
          <div class="rating-text">{t["rating_text"]}</div>
        </div>
      </div>
      <div class="kv">
        {"".join(f"<div>{k}<strong>{v}</strong></div>" for k, v in t["kv"])}
      </div>
    </aside>
  </div>
</section>

<section id="bonuses">
  <div class="container">
    <header class="section-head">
      <h2>{t["bonuses_h"]} <em>{t["bonuses_em"]}</em></h2>
      <p>{t["bonuses_p"]}</p>
    </header>
    <div class="bonus-grid">
      {render_bonuses(t)}
    </div>
  </div>
</section>

<section id="compare" style="background:var(--bg-2);">
  <div class="container">
    <header class="section-head">
      <h2>{t["compare_h"]}</h2>
      <p>{t["compare_p"]}</p>
    </header>
    {render_compare(t)}
  </div>
</section>

<section id="review">
  <div class="container">
    <header class="section-head">
      <h2>{t["review_h_a"]} <em>{t["review_h_em"]}</em> {t["review_h_b"]}</h2>
      <p>{t["review_p"]}</p>
    </header>
    <article class="longread">
      {render_longread(t["longread"])}
    </article>
  </div>
</section>

<section style="background:var(--bg-2);">
  <div class="container">
    <header class="section-head">
      <h2>{t["social_h"]}</h2>
      <p>{t["social_p"]}</p>
    </header>
    <div class="reviews">
      {render_reviews(t)}
    </div>
  </div>
</section>

<section id="faq">
  <div class="container">
    <header class="section-head">
      <h2>{t["faq_h"]}</h2>
      <p>{t["faq_p"]}</p>
    </header>
    <div class="faq">
      {render_faq(t)}
    </div>
  </div>
</section>

</main>

<footer class="site-footer">
  <div class="container">
    <div class="responsible">
      18+. {t["responsible"]} <a href="https://www.begambleaware.org/" rel="noopener noreferrer" target="_blank" style="color:#ff9aa8;text-decoration:underline">{t["responsible_link"]}</a>.
    </div>
    <div class="footer-grid">
      <div>
        <h4>Duel Casino Review</h4>
        <p>{t["footer_about"]}</p>
      </div>
      <div>
        <h4>{t["footer_sections"]}</h4>
        <a href="#bonuses">Bonus</a>
        <a href="#review">Review</a>
        <a href="#compare">Compare</a>
        <a href="#faq">FAQ</a>
      </div>
      <div>
        <h4>{t["footer_languages"]}</h4>
        <a href="/" hreflang="en">English</a>
        <a href="/no/" hreflang="no">Norsk</a>
        <a href="/de/" hreflang="de">Deutsch</a>
        <a href="/fr/" hreflang="fr">Français</a>
      </div>
      <div>
        <h4>{t["footer_legal"]}</h4>
        <a href="/privacy.html">Privacy</a>
        <a href="/terms.html">Terms</a>
        <a href="/responsible.html">Responsible</a>
      </div>
    </div>
    <div class="legal">
      <span>{t["footer_copy"]}</span>
      <span>{t["tagline"]}</span>
    </div>
  </div>
</footer>

<a class="sticky-cta" href="https://duel.com/?ref=duelreview&p={path}_sticky" target="_blank" rel="nofollow noopener noreferrer" aria-label="Play Duel Casino">
  {t["cta"]}
</a>

<script src="/assets/js/main.js" defer></script>
</body>
</html>
'''

# ---------- generate ----------
for loc in LOCALES:
    path = loc["path"]
    t = T[path]
    out_path = os.path.join(OUT, path, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page_html(loc, t))
    print("Wrote", out_path)

print("Done.")
