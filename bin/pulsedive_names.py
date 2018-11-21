#!/opt/splunk/bin/python

feeds = [
	"Zeus Bad Domains",
	"Zeus Bad IPs",
	"TOR IPs",
	"C&C IPs",
	"Ransomware Domains",
	"Ransomware IPs",
	"Cridex IPs",
	"Dyre Botnet IPs",
	"SSL BL",
	"CI Bad Guys",
	"Bad IPs",
	"BBcan177 DNSBL",
	"Brute Force Blocker",
	"Darklist",
	"GreenSnow Blacklist",
	"IPSpamList",
	"Dictionary SSH Attacks",
	"OpenPhish",
	"Suspicious Domains",
	"Domains Blacklist",
	"Suspicious Dynamic DNS Providers",
	"Malware Domains",
	"Malware Domains List",
	"Feodo Tracker",
	"Immortal Malware Domains",
	"C&C Domains",
	"PhishTank",
	"Botvrij.eu - domains",
	"Botvrij.eu - hostnames",
	"Botvrij.eu - ips",
	"Alienvault IP Reputation",
	"Talos IP Blacklist",
	"Ransomware URLs",
	"High Confidence IPv4 Drop List",
	"Blocklist.de Blocklist",
	"Malicious EXE URLs",
	"Malicious EXE IPs",
	"Botvrij.eu - urls",
	"URLhaus",
	"Compromised IPs",
	"Malware Corpus Tracker",
	"Simple Malware List",
	"Monero Miner",
	"NoCoin",
	"CoinBlocker Domains",
	"ZeroDot1's Bad IPs Feed",
	"BBcan177 Malicious IPs",
	"Hancitor IPs",
]

threats = [
	"Zeus",
	"TOR Proxy",
	"Banjori",
	"Shiotob",
	"Bedep",
	"Beebone",
	"Kraken Botnet",
	"Matsnu",
	"Necurs",
	"Nymaim",
	"Pizd",
	"Proslikefan",
	"Pykspa",
	"Ramdo",
	"Ramnit",
	"Simda",
	"Suppobox",
	"Tiny Banker",
	"unknownjs",
	"Vawtrak",
	"Virut",
	"Dyre",
	"TrickBot",
	"Adwind",
	"PandaZeuS",
	"Quakbot",
	"Malware",
	"Smoke Loader",
	"Shylock",
	"Gootkit",
	"Qadars",
	"SSH Brute Force",
	"Telnet",
	"SMTP Attack",
	"MS-DS Attack",
	"RDP Attack",
	"Proxy Scan",
	"SIP Attacks",
	"Unclassified",
	"Postfix",
	"MS-SQL Attack",
	"FTP",
	"MySQL Attack",
	"Netbios Attack",
	"Socks Scan",
	"RpcBind Attack",
	"Ranbyus",
	"Mirai",
	"VNC Attack",
	"IMAP3 Attack",
	"POP Attack",
	"RPC-WIN Attack",
	"AKBuilder",
	"POPS Attack",
	"Comment Spam",
	"Locky",
	"Web Hacking",
	"Phishing",
	"Dridex",
	"Wannacry",
	"Dircrypt",
	"Fobber",
	"Hesperbot",
	"Murofet",
	"Gozi",
	"IMAP",
	"Cutwail",
	"Bitcoin.Scammer",
	"Sphinx",
	"Cobalt",
	"X-Windows Attack",
	"Kovtar",
	"Adware",
	"Dreambot",
	"AZORult",
	"Bamital",
	"QuantLoader",
	"CyberGhost VPN",
	"AgentTesla",
	"Pony",
	"Andromeda",
	"Hancitor",
	"GandCrab",
	"CryptoLocker",
	"GameOver Zeus",
	"JS Crypto Miner",
	"Monero",
	"SynAck",
	"LokiBot",
	"Netwire",
	"IIS Attack",
	"FormBook",
	"Nuclear Exploit Kit",
	"Conficker",
	"Zoopark",
	"StealthAgent",
	"Crimson",
	"Operation Transparent Tribe",
	"Enigma",
	"xTreme RAT",
	"Nanobot",
	"VPNFilter",
	"APT28",
	"Grandsoft",
	"RIG",
	"Trojan-Downloader.NSIS",
	"Symmi",
	"Sarvdap",
	"DanaBot",
	"Hidden Cobra",
	"Troj.Downloader.W32.Mediaget",
	"CVE-2016-5426",
	"SamSam",
	"Win32.Trojan.WisdomEyes",
	"Petya",
	"IcedId",
	"AzorUlt Version 2",
	"TROJ_GEN.R020C0PF718",
	"Win32:Dropper-FSB [Drp]",
	"Invisimole",
	"MSIL",
	"p2pgoz",
	"qakbot",
	"Android Trojan",
	"Kardon Loader",
	"NanoCore RAT",
	"qrat",
	"Neutrino",
	"Emotet",
	"tofsee",
	"Android malware",
	"Sality",
	"Spamming",
	"Cryptojacking",
	"Executable Code",
	"Spear Phishing",
	"Coinhive",
	"CoinImp",
	"Rapid",
	"Remcos RAT",
	"Hupigon",
	"Godzilla",
	"MoneyTaker",
	"RemoteAdmin.RemoteUtilities.A",
	"Win32.Trojan.Agent",
	"Trojan.BAT.Agent",
	"PushIran.DL",
	"Qealler",
	"CVE-2018-11776",
	"Predatorstealer",
	"Dharma",
	"Razy",
	"Graftor",
	"Bladabindi",
	"UrlMal",
	"Vigorf",
	"Barys",
	"Ursu",
	"Strictor",
	"Swrort",
	"Themida",
	"Zusy",
	"Fuery",
	"Spursint",
	"Kryptik",
	"NetFilter",
	"FileProxy",
	"FileTour",
	"Androm",
	"iBryte",
	"Mimikatz",
	"Stratos",
	"FAREIT",
	"Perseus",
	"Liusky",
	"Shelma",
	"HPLOKI",
	"GlobeImposter",
	"Sohanad",
	"Mikey",
	"Eorezo",
	"Certutil",
	"Silence",
	"Bad Rabbit",
	"Domestic Kitten (Iranian Group)",
	"RevCodeRAT",
	"MalDoc",
	"Artemis",
	"Rozena",
	"Krypt",
	"Kazy",
	"Philadelphia",
	"Evo",
	"Shellbot",
	"Adposhel",
	"Addrop",
	"Cduit",
	"Swisyn",
	"Bodegun",
	"RevengeRat",
	"Johnnie",
	"Dorifel",
	"ServStart",
	"Asparnet",
	"CandyOpen",
	"NetSup",
	"EmoooDld",
	"XSSShell",
	"AutoHK",
	"AFRF",
	"Gafgyt",
	"Presenoker",
	"CozyDuke",
	"OnionDuke",
	"Csfrsys",
	"Rebhip",
	"Hiddentear",
	"Ekisoli",
	"DynAmite",
	"Bitpaymer",
	"Ryuk",
	"Shade",
	"KillRabit",
	"Nemucod",
	"Carberp",
	"Tovkater",
	"unknowndropper",
	"Valyria",
	"TorJok",
	"SASL_Brute_Force",
	"CVE-2017-11882",
	"PlugX",
	"SASL_Bruteforce",
	"Open Directory",
	"ZapSpot",
	"BitCoinMiner",
	"DarkKomet",
	"Trojan",
	"Nemesis",
	"OrcusRAT",
	"CoinMiner",
	"Magecart",
	"tempedreve",
	"volatile cedar / explosive",
]
