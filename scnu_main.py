import csv
from scnu_save import extract_indeed_pages
from scnu_save import extract_job

def make_csv(jobs):
  file = open("scnu_scrapping.csv",mode="w",encoding='cp949')
  writer = csv.writer(file)
  writer.writerow(["title","link"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return

done_csv1 = extract_job(extract_indeed_pages())
make_csv(done_csv1)
