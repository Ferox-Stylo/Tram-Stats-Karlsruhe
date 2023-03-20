def create_tram_stats(tram: str, color: str, percent: int, one_time_1: float, one_time_7: float, one_time_30: float,
                      one_time_356: float, to_late_1: float, to_late_7: float, to_late_30: float, to_late_356: float,
                      cancelled_1: int, cancelled_7: int, cancelled_30: int, cancelled_356: int, average_1: float,
                      average_7: float, average_30: float, average_356: float, total_1: int, total_7: int,
                      total_30: int, total_356: int) -> str:
    dash_offset = 501 - (5.01 * percent)

    return f'<svg width="600" height="350">\n' + \
        f'<svg width="580" height="330">' + \
        f'<rect width="580" height="330" style="fill:rgb(30,40,57);" />' + \
        f'<rect x="10" y="70" width="180" height="120" style="fill:rgb(66, 89, 126);"/>' + \
        f'<rect x="10" y="200" width="180" height="120" style="fill:rgb(66, 89, 126);"/>' + \
        f'<rect x="200" y="70" width="180" height="120" style="fill:rgb(66, 89, 126);"/>' + \
        f'<rect x="200" y="200" width="180" height="120" style="fill:rgb(66, 89, 126);"/>' + \
        f'<rect x="390" y="200" width="180" height="120" style="fill:rgb(66, 89, 126);"/>' + \
        f'<circle cx="480" cy="100" r="70" fill="{color}" />' + \
        f'<circle stroke-linecap="round" cx="0" cy="480" r="80" stroke="red" stroke-width="4" fill="none" ' \
        f'stroke-dasharray="501" stroke-dashoffset="{dash_offset}" transform="rotate(-90 ) translate(-100 0)" />' + \
        f'<text x="15" y="40" fill="white" font-size="2em" font-weight="700">Stats for Tram Line {tram}</text>' + \
        f'<text x="435" y="120" fill="white" font-size="4em" font-weight="700">{tram}</text>' + \
        f'<text x="15" y="95" fill="white" font-size="1.3em" font-weight="700">On Time</text>' + \
        f'<text x="25" y="120" fill="white" font-size="1.1em">Last 24h: {one_time_1}</text>' + \
        f'<text x="25" y="140" fill="white" font-size="1.1em">Last 7d: {one_time_7}</text>' + \
        f'<text x="25" y="160" fill="white" font-size="1.1em">Last 30d: {one_time_30}</text>' + \
        f'<text x="25" y="180" fill="white" font-size="1.1em">Last 356d: {one_time_356}</text>' + \
        f'<text x="15" y="225" fill="white" font-size="1.3em" font-weight="700">To Late</text>' + \
        f'<text x="25" y="245" fill="white" font-size="1.1em">Last 24h: {to_late_1}</text>' + \
        f'<text x="25" y="265" fill="white" font-size="1.1em">Last 7d: {to_late_7}</text>' + \
        f'<text x="25" y="285" fill="white" font-size="1.1em">Last 30d: {to_late_30}</text>' + \
        f'<text x="25" y="305" fill="white" font-size="1.1em">Last 356d: {to_late_356}</text>' + \
        f'<text x="205" y="95" fill="white" font-size="1.3em" font-weight="700">Cancelled</text>' + \
        f'<text x="215" y="120" fill="white" font-size="1.1em">Last 24h: {cancelled_1}</text>' + \
        f'<text x="215" y="140" fill="white" font-size="1.1em">Last 7d: {cancelled_7}</text>' + \
        f'<text x="215" y="160" fill="white" font-size="1.1em">Last 30d: {cancelled_30}</text>' + \
        f'<text x="215" y="180" fill="white" font-size="1.1em">Last 356d: {cancelled_356}</text>' + \
        f'<text x="205" y="225" fill="white" font-size="1.3em" font-weight="700">Average Delay</text>' + \
        f'<text x="215" y="245" fill="white" font-size="1.1em">Last 24h: {average_1}</text>' + \
        f'<text x="215" y="265" fill="white" font-size="1.1em">Last 7d: {average_7}</text>' + \
        f'<text x="215" y="285" fill="white" font-size="1.1em">Last 30d: {average_30}</text>' + \
        f'<text x="215" y="305" fill="white" font-size="1.1em">Last 356d: {average_356}</text>' + \
        f'<text x="395" y="225" fill="white" font-size="1.3em" font-weight="700">Total Trams</text>' + \
        f'<text x="405" y="245" fill="white" font-size="1.1em">Last 24h: {total_1}</text>' + \
        f'<text x="405" y="265" fill="white" font-size="1.1em">Last 7d: {total_7}</text>' + \
        f'<text x="405" y="285" fill="white" font-size="1.1em">Last 30d: {total_30}</text>' + \
        f'<text x="405" y="305" fill="white" font-size="1.1em">Last 356d: {total_356}</text>' + \
        f'</svg>\n' + \
        f'</svg>'


svg_image = create_tram_stats("S11", "green", 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
print(svg_image)
