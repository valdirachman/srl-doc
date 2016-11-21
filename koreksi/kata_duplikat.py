import re
fileNames = [
'../abstract.tex',
'../abstrak.tex',
'../bab1.tex',
'../bab2.tex',
'../bab3.tex',
'../bab4.tex',
'../bab5.tex',
'../bab6.tex',
'../daftarsingkatan.tex',
'../hype.indonesia.tex',
'../istilah.tex',
'../judul_dalam.tex',
'../lampiran.tex',
'../laporan_setting.tex',
'../markLampiran.tex',
'../orisinal.tex',
'../pengantar.tex',
'../pengesahan_sidang.tex',
'../pengesahan.tex',
'../persetujuan_publikasi.tex',
'../sampul.tex',
'../skripsi.tex', ]
for fn in fileNames:
  print(fn)
  with open(fn) as f: listKata = f.read().split()
  for d in range(1,4):
    for i in range(len(listKata)-d):
      wLeft = listKata[i]#.upper()
      wRight = listKata[i+d]#.upper()
      if len(wLeft) < 2 or len(wLeft) > 50: continue
      if wLeft == wRight and re.fullmatch(r'[^\\]*[a-z].*',wLeft) != None:
        print(' '.join([wLeft]+listKata[i+1:i+d]+[wRight]))
  print('\n')