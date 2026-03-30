import os
import requests

GITHUB_LANG_COLORS = {
    "1C Enterprise":"#814CCC","ABAP":"#E8274B","ActionScript":"#882B0F",
    "Ada":"#02f88c","Agda":"#315665","AGS Script":"#B9D9FF","AL":"#3AA2B5",
    "Alloy":"#64C800","ANTLR":"#9DC3FF","AppleScript":"#101F1F","Arc":"#aa2afe",
    "Arduino":"#bd79d1","ASP.NET":"#9400ff","AspectJ":"#a957b0","Assembly":"#6E4C13",
    "ATS":"#1ac620","AutoHotkey":"#6594b9","AutoIt":"#1C3552","Awk":"#c30e9b",
    "Ballerina":"#FF5000","Bash":"#89e051","Batchfile":"#C1F12E","Beef":"#a52f4e",
    "Bison":"#6A463F","Blade":"#f7523f","BlitzBasic":"#00FFAE","BlitzMax":"#cd6400",
    "Boo":"#d4bec1","Brainfuck":"#2F2530","C":"#555555","C#":"#178600",
    "C++":"#f34b7d","Ceylon":"#dfa535","Chapel":"#8dc63f","Cirru":"#ccccff",
    "Classic ASP":"#6a40fd","Clean":"#3F85AF","Clojure":"#db5855","CoffeeScript":"#244776",
    "ColdFusion":"#ed2cd6","Common Lisp":"#3fb68b","Component Pascal":"#B0CE4E",
    "Crystal":"#000100","CSS":"#563d7c","Cuda":"#3A4E3A","D":"#ba595e",
    "Dart":"#00B4AB","Dhall":"#dfafff","Dockerfile":"#384d54","Dylan":"#6c616e",
    "E":"#ccce35","Eiffel":"#4d6977","Elixir":"#6e4a7e","Elm":"#60B5CC",
    "Emacs Lisp":"#c065db","EmberScript":"#FFF4F3","Erlang":"#B83998",
    "F#":"#b845fc","F*":"#572e30","Factor":"#636746","Fennel":"#fff3d7",
    "Forth":"#341708","Fortran":"#4d41b1","FreeMarker":"#0050b2","Frege":"#00cafe",
    "Futhark":"#5f021f","Game Maker Language":"#71b417","GLSL":"#5686a5",
    "Gnuplot":"#f0a9f0","Go":"#00ADD8","Golo":"#88562A","Gosu":"#82937f",
    "Groovy":"#e69f56","Hack":"#878787","Haml":"#ece2a9","Handlebars":"#f7931e",
    "Haskell":"#5e5086","Haxe":"#df7900","HCL":"#844FBA","HLSL":"#aace60",
    "HTML":"#e34c26","Hy":"#7790B2","IDL":"#a3522f","Idris":"#b30000",
    "Io":"#a9188d","J":"#9EEDFF","Java":"#b07219","JavaScript":"#f1e05a",
    "Jinja":"#a52a22","Julia":"#a270ba","Jupyter Notebook":"#DA5B0B","Kotlin":"#A97BFF",
    "LabVIEW":"#fede06","Lasso":"#999999","Less":"#1d365d","Lex":"#DBCA00",
    "LFE":"#4C3023","LilyPond":"#9ccc7c","Liquid":"#67b8de","LiveScript":"#499886",
    "LLVM":"#185619","Logtalk":"#295b9a","LookML":"#652B81","Lua":"#000080",
    "Makefile":"#427819","Mako":"#7e858d","Markdown":"#083fa1","Marko":"#42bff2",
    "MATLAB":"#e16737","Mercury":"#ff2b2b","Meson":"#007800","Metal":"#8f14e9",
    "Mirah":"#c7a938","MoonScript":"#ff4585","MQL4":"#62A8D6","MQL5":"#4A76B8",
    "Mustache":"#724b3b","Nit":"#009917","Nix":"#7e7eff","NumPy":"#9C8AF9",
    "Objective-C":"#438eff","Objective-C++":"#6866fb","Objective-J":"#ff0c5a",
    "OCaml":"#3be133","Odin":"#60AFFE","ooc":"#b0b77e","OpenCL":"#ed2e2d",
    "OpenSCAD":"#e5cd45","Ox":"#FF7C00","Opal":"#f7ede0","Oxygene":"#cdd0e3",
    "Oz":"#fab738","P4":"#7055b5","Papyrus":"#6600cc","Parrot":"#f3ca0a",
    "Pascal":"#E3F171","Pawn":"#dbb284","Perl":"#0298c3","PHP":"#4F5D95",
    "Pike":"#005390","PLpgSQL":"#336790","PLSQL":"#dad8d8","PostScript":"#da291c",
    "PowerShell":"#012456","Prolog":"#74283c","Pug":"#a86454","Puppet":"#302B6D",
    "PureBasic":"#5a6986","PureScript":"#1D222D","Python":"#3572A5","Q#":"#fed659",
    "R":"#198CE7","Racket":"#3c5caa","Ragel":"#9d5200","Raku":"#0000fb",
    "Reason":"#ff5847","Red":"#f50000","Ring":"#2D54CB","RobotFramework":"#00c0b5",
    "Ruby":"#701516","Rust":"#dea584","Scala":"#c22d40","Scheme":"#1e4aec",
    "Scilab":"#ca0f21","Self":"#0579aa","Shell":"#89e051","Slim":"#2b2b2b",
    "Smalltalk":"#596706","Solidity":"#AA6746","SQL":"#e38c00","Squirrel":"#800000",
    "Stan":"#b2011d","Stata":"#1a5f91","SuperCollider":"#46390b","Svelte":"#ff3e00",
    "Swift":"#F05138","SystemVerilog":"#DAE1C2","Tcl":"#e4cc98","Terra":"#00004c",
    "Thrift":"#D12127","TSQL":"#e9a84c","TSX":"#2b7489","Turing":"#cf142b",
    "TypeScript":"#2b7489","Uno":"#9933cc","V":"#4f87c4","Vala":"#fbe5cd",
    "VBA":"#867db1","VBScript":"#15dcdc","Verilog":"#b2b7f8","VHDL":"#adb2cb",
    "Vim Script":"#199f4b","Vim script":"#199f4b","Visual Basic .NET":"#945db7",
    "Vue":"#41b883","WebAssembly":"#04133b","Wren":"#383838","XC":"#99DA07",
    "Xojo":"#81bd41","XQuery":"#5232e7","XSLT":"#EB8CEB","Yacc":"#4B6C4B",
    "YAML":"#cb171e","Zephir":"#118f9e","Zig":"#ec915c",
}

FALLBACK_COLORS = ["#4ec9b0","#b5cea8","#D3C6AA","#81c784","#6dbfa0","#a8c4b0"]


def lang_color(name: str, idx: int) -> str:
    return GITHUB_LANG_COLORS.get(name, FALLBACK_COLORS[idx % len(FALLBACK_COLORS)])


def fetch_languages(username: str, token: str) -> dict[str, int]:
    query = """
    query($login: String!, $after: String) {
      user(login: $login) {
        repositories(
          first: 100 after: $after
          ownerAffiliations: OWNER isFork: false
        ) {
          pageInfo { hasNextPage endCursor }
          nodes {
            languages(first: 25, orderBy: {field: SIZE, direction: DESC}) {
              edges { size node { name } }
            }
          }
        }
      }
    }
    """
    headers = {"Authorization": f"bearer {token}", "Content-Type": "application/json"}
    totals: dict[str, int] = {}
    after = None

    while True:
        resp = requests.post(
            "https://api.github.com/graphql",
            headers=headers,
            json={"query": query, "variables": {"login": username, "after": after}},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        if "errors" in data:
            raise RuntimeError(f"GraphQL errors: {data['errors']}")

        repos = data["data"]["user"]["repositories"]
        for repo in repos["nodes"]:
            for edge in repo["languages"]["edges"]:
                totals[edge["node"]["name"]] = totals.get(edge["node"]["name"], 0) + edge["size"]

        if not repos["pageInfo"]["hasNextPage"]:
            break
        after = repos["pageInfo"]["endCursor"]

    return totals


def build_svg(lang_totals: dict[str, int], top_n: int = 8) -> str:
    sorted_langs = sorted(lang_totals.items(), key=lambda x: x[1], reverse=True)[:top_n]
    total = sum(b for _, b in sorted_langs)
    if not total:
        return "<svg/>"

    langs = [
        {"name": n, "pct": round(b / total * 100, 1), "color": lang_color(n, i)}
        for i, (n, b) in enumerate(sorted_langs)
    ]

    # ── Your color palette ───────────────────────────────────────────────
    TITLE_COLOR  = "#4ec9b0"   # teal
    TEXT_COLOR   = "#b5cea8"   # sage green
    PCT_COLOR    = "#b5cea8"   # same sage for %
    TRACK_COLOR  = "#1a3a1a"   # slightly lighter than bg so track is visible
    BG           = "#0D1F0D"   # flat dark green
    FONT         = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"

    # ── Layout ────────────────────────────────────────────────────────────
    W        = 400
    PAD_X    = 26
    TITLE_H  = 58
    ROW_H    = 46
    CORNER   = 20
    DOT_R    = 6
    BAR_H    = 7
    BAR_R    = 4
    NAME_W   = 90
    PCT_W    = 48                              # fixed slot for % label
    BAR_X    = PAD_X + DOT_R * 2 + 10 + NAME_W
    BAR_W    = W - BAR_X - PAD_X - PCT_W      # bar always ends before % label
    PCT_X    = W - PAD_X                       # % right-aligned

    H = TITLE_H + len(langs) * ROW_H + 18

    rows = []
    for i, lang in enumerate(langs):
        cy   = TITLE_H + i * ROW_H + ROW_H // 2
        c    = lang["color"]
        fw   = max(6, round(BAR_W * lang["pct"] / 100, 1))
        ty   = cy + 5

        rows.append(f"""
  <circle cx="{PAD_X + DOT_R}" cy="{cy}" r="{DOT_R}" fill="{c}"/>
  <text x="{PAD_X + DOT_R*2 + 10}" y="{ty}"
        font-family="{FONT}" font-size="13" font-weight="600"
        fill="{TEXT_COLOR}">{lang["name"]}</text>
  <rect x="{BAR_X}" y="{cy - BAR_H//2}" width="{BAR_W}" height="{BAR_H}"
        rx="{BAR_R}" fill="{TRACK_COLOR}"/>
  <rect x="{BAR_X}" y="{cy - BAR_H//2}" width="{fw}" height="{BAR_H}"
        rx="{BAR_R}" fill="{c}" opacity="0.75"/>
  <text x="{PCT_X}" y="{ty}"
        font-family="{FONT}" font-size="12" font-weight="600"
        fill="{PCT_COLOR}" text-anchor="end">{lang["pct"]}%</text>""")

    return f"""<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}"
     xmlns="http://www.w3.org/2000/svg" role="img"
     aria-label="Most Used Languages">

  <rect width="{W}" height="{H}" rx="{CORNER}" fill="{BG}"/>

  <text x="{PAD_X}" y="36"
        font-family="{FONT}" font-size="18" font-weight="700"
        fill="{TITLE_COLOR}" letter-spacing="0.2">Most Used Languages</text>

  {"".join(rows)}
</svg>"""


def main():
    token    = os.environ["GH_TOKEN"]
    username = os.environ["GH_USERNAME"]
    top_n    = int(os.environ.get("TOP_N", "8"))
    out      = os.environ.get("OUTPUT_PATH", "assets/langs-card.svg")

    print(f"Fetching language stats for @{username}…")
    totals = fetch_languages(username, token)
    print(f"Found {len(totals)} languages.")

    svg = build_svg(totals, top_n=top_n)
    os.makedirs(os.path.dirname(out) if os.path.dirname(out) else ".", exist_ok=True)
    with open(out, "w") as f:
        f.write(svg)
    print(f"Written → {out}")


if __name__ == "__main__":
    main()
