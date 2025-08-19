import urllib.request, json, math
def hae_kaikki():
	t = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
	data = json.loads(t.read())
	return [(i["fullName"], i["name"], i["year"], sum(i["exercises"])) for i in data if i["enabled"]]

def hae_kurssi(kurssi: str):
	t = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{kurssi}/stats")
	data = json.loads(t.read())
	opiskelijoita = max(int(i["students"]) for i in data.values())
	tunteja = sum(i["hour_total"] for i in data.values())
	tehtavia = sum(i["exercise_total"] for i in data.values())
	return {
		"viikkoja": len(data),
		"opiskelijoita": opiskelijoita,
		"tunteja": tunteja,
		"tunteja_keskimaarin": math.floor(tunteja / opiskelijoita),
		"tehtavia": tehtavia,
		"tehtavia_keskimaarin": math.floor(tehtavia / opiskelijoita),
	}

if __name__ == "__main__":
	hae_kaikki()
	print(hae_kurssi("docker2019"))