#!/bin/bash/env python3
"""
This python script extracts a passphrase from a matrix of encrypted text
- You will need to convert vertical text back to horizontal.
- Clue: Treat the string of text like a matrix and transpose it. The keyword here is TRANSPOSE.
- Clue: there is fixed width/row:55 and hight/column:36.
- Clue: Write a regex to replace the symbols with a single space to get the password.
"""

def is_letter(letter):
    try:
        return letter.isalpha()
    except:
        return False

def remove_excess_spaces(string):
    string = string.split()
    cleanstring = ""
    for i in string:
        cleanstring += i + " "
    return cleanstring

def transpose_matrix(old):
    new = []
    for i in range(55):
        newrow = []
        for j in range(36):
            newrow.append( old[j][i] )
        new.append(newrow)
    return new

def main():
    # Copy the text at the bottom into a file called matrix
    rawfile = open('C:\\Users\\James\\Desktop\\sandbox\\encrypt\\matrix.txt', 'r')
    rawmatrix = []
    for line in rawfile.readlines():
        row = []
        for char in line:
            if is_letter(char):
                row.append(char)
            else:
                row.append(' ')
        rawmatrix.append(row)


    newmatrix = transpose_matrix(rawmatrix)
    zip_file_password = ""
    for i in range(55):
        for j in range(36):
            zip_file_password += newmatrix[i][j]

    zip_file_password = remove_excess_spaces(zip_file_password)
    print(zip_file_password)


if __name__ == "__main__":
    main()

# Below is the "matrix that needs to be read in from a file"
"""
Irnmckr^ $#nrcg %*e(_*ihrd_snfEd)t%ed+erh+!e)_h*%hc%au)
c&)aho#eda$i%he^@hvb+mt_ a(&eose$ s+c&!de_&id@t#zehtlr%
h%!cin!sin^c)+w*!aoe(it*)r!%ilsri+i@h$*en@+de^_%urtulcf
#zuhgn&%ezdh$%aSDtrv$ce)bu #dge*n$c!e ^_@Bk(n(H  +enehu
^umeetg+(oit_*gtu%(o*hn(obs(ee*a(zh)nE)aSlo%_hai)^+%$+r
h +nree_!ge(d^tusd!rg#% set rn(u!u$ ssibiint%aun^_&_S^%
a@_%@%s$se!)i#ehca)*a^(veratn*$fd ^k$+heecnu ts_%d!aye#
b+G_N#t*cn@*elslhc @b* o+_rr##_ e& om_rr*ktt$(e++iWlmi)
e(e(e(avh)#&^a&#eh_%%uIr#@ku$@d^rA!niwe@%&e)!^r$uealbn@
@br#r!pil*wI!n +&te+_mc#!($b!$a@#nanran(#!+@d n%n!ceo_d
_eb dieeedic)d+__er&e$h)n!#egwn!s+utsr))d+)di@^!t*hsl)a
&hew)nllcirhwe$(^_)dr@__ea@&eondo_se_eE^e*#aee!de(t(e@s
varo!(tlhe!!atGH!& u**#dtngTw_%ere^n#@h_nd!s i%er_e!+*)
ole (d_et^$hc(ue ^%_!(wettera!Dmgi*(@!es e(s%n_rr@rw) !
rtisae)ie)Oah*tyz$s+#_am!wsoc(a^lf!d ama(nd @( ^idsa(e#
be)imnhc&*hbs_e_u%i&%Wr#wocsh#n_or%a$uag!^a(_^ilcats&i&
en$c_&ah__aeais&sSc &ot^erhts$n%siuspcnem+#+P+sahco*#nP
i$#h$_tt(K) mh!#aeh)ihe itl&em &egm@ahnni$!@eTtnthl+uza
g+__^$t!@lb*%r+wmr fhltTlea@na+Bn@&B&#* td%)rr$getz$nis
edl@Mee+Gei(* )omv#lnbeo#sf^_g$e#(!um!d)$e^sse!sne^ dgs
sia)or#&rit^_b^$eu)e&e$rdte+(dst_s^cusoS*r@eop#a+n!S*ew
ceu*r#$#antv+e@%ns$czf)*u*ngueat+t%h#crie(einp^m_@)i+so
h negjadueeissns()%hui_%^!$ambh_!r$&(hteiKsn$eAe&L$eL*r
aziieebasnreiteo!@ntrn%w*d%b)e)& es*!o$$nu(^)nbn!as e)t
uusnnmesa+_lnebr+&eeudba(a+*%tdsScp$^nh_en*L he Ksete$)
t*c#%arsm!)edneg^*unceerbsh&+tetoka))$a^md@aear+l#iurLz
_^h+al&%k)s%)fnlg!$)knvtesam_$rartrdawl#^e_biu*&aS+nzeu
^m*!ns%+e(a&%a+oehf ( oes&siz jngesenet@s $sns_(ras(ee*
ui&&z@!$i u* l$ssarw)*rts#ttu^edl!assneta^mag$ Tega_ire
mrz i*# tag_Pl! cleo+&(eed@()(n$o&m)pnnin)ile_nr_eu!czr
&+uge_e*ent^ls^!hbulu%+@rud* si*se$%r(*ef$r-lmieHrb$hes
B%$ehBrBnzeMo@ *a!tlmz^^()a++ag isp_e)@fth(Paiepuee)eie
ik@seu$a)onat+d^u#et_u &^!s$^(e&g+a$c@$!ea ldtmptirunct
la(pnrml+g*rz&edt_ e@@%$$ssSv$#!k*)@h^)_nb@ae%aem*+m@hz
dm%r@gal@e+dl*mi(&#s _iw*o&ce^+Je SMesws&e!tnal*ad@^$ee
ee)a_ege!n!ei()e^b+t^bca)$ehr%&ai^ianiue*nlz%cs_ca#)dnn

"""