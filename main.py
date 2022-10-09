import random
import os

os.system('cls')

class name():
    
    os.system('cls')
    
    gen = ['masc', 'fem']        
    
    gender = random.choice(gen)
    
    os.system('cls')
    
    if gender == 'masc':
        print ('Genêro: Masculino')
        with open ('masc_names.txt', 'r') as masc_names:
            names = masc_names.readlines()
            esc = random.choice(names)
            print ('Nome: {}'.format(esc))
 
    if gender == 'fem':
        print ('Genêro: Feminino')
        with open ('fem_names.txt', 'r') as fem_names:
            names = fem_names.readlines()
            esc = random.choice(names)
            print ('Nome: {}'.format(esc))

class age():
    
    age = random.randint(18, 35)
    print ('Idade: {}'.format(age))
    
class sex():
    
    with open ('sexual.txt', 'r') as sex_op:
        sex_list = sex_op.readlines()
        esc = random.choice(sex_list)
        print ('Sexualidade: {}'.format(esc))

class prof():
    with open ('profiss.txt', 'r') as profs:
        prof_list  = profs.readlines()
        esc = random.choice(prof_list)
        print ('Profissão: {}'.format(esc))

class apr():
    
    #cabelo
    with open ('ap_CABELO.txt', 'r') as hair:
        hair_list = hair.readlines()
        esc = random.choice(hair_list)
        print ('Cabelo {}'.format(esc))
        
    #olho
    with open ('ap_OLHO.txt', 'r') as eye:
        eye_list = eye.readlines()
        esc = random.choice(eye_list)
        print ('Olho {}'.format(esc))
        
    #pele
    with open ('ap_PELE.txt', 'r') as skin:
        skin_list = skin.readlines()
        esc = random.choice(skin_list)
        print ('Pele {}'.format(esc))
        
    #roupa_superior
    with open ('ap_ROUPA_SUP.txt', 'r') as up_clo:
        up_clo_list = up_clo.readlines()
        esc = random.choice(up_clo_list)
        print (esc)
        
    #roupa_inferior
    with open ('ap_ROUPA_INF.txt', 'r') as inf_clo:
        inf_clo_list = inf_clo.readlines()
        esc = random.choice(inf_clo_list)
        print (esc)
        
    #roupa_extra
    with open ('ap_ROUPA_EXT.txt', 'r') as ext_clo:
        ext_clo_list = ext_clo.readlines()
        esc = random.choice(ext_clo_list)
        print (esc)

class pers():
     
    with open ('perso.txt', 'r') as person:
        pers_op_list = person.readlines()
        esc = random.sample(pers_op_list, k=3)
        print ('{}'.format(esc))
        
class hist_b():
    with open ('hist_b_elements.txt', 'r') as hist_base:
        hist_b_el_list = hist_base.readlines()
        esc = random.choice(hist_b_el_list)
        print ('Hisória base: {}'.format(esc))

class hist_p():
    with open ('hist_p_elements.txt', 'r') as hist_p:
        hist_p_el_list = hist_p.readlines()
        esc = random.choice(hist_p_el_list)
        print ('História com o paranormal: {}'.format(esc))
        
class inv():
    with open ('items.txt', 'r') as item:
        itens_list = item.readlines()
        esc = random.sample(itens_list, k=3)
        print ('Itens: {}'.format(esc))
        
class pp():
    
    carisma = 1
    agilidade = 1
    intelecto = 1
    vigor = 1
    forca = 1
    
    list = ['carisma', 'agilidade', 'intelecto', 'vigor', 'forca']
    
    esc = random.sample(list, k=2)
    print ('{} = 2 '.format(esc))

class clas():
    
    with open ('class_list.txt', 'r') as class_l:
        classs_list = class_l.readlines()
        esc = random.choice(classs_list)
        
        if esc == 'Combatente':
            
            with open ('subclass_comb.txt', 'r') as subcomb:
                sub_comb_list = subcomb.readlines()
                esco_subc = random.choice(sub_comb_list)
                
                if esco_subc == 'Atirador':
                    with open ('subclass_tri-atirador.txt') as tri_ati:
                        tri_list = tri_ati.readlines()
                        tri_esc = random.choice(tri_list)
                        
                        if tri_esc == 'Mercenario':
                        
                            print ('Classe: Combatente / Subclasse: Atirador (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 forca / +1 luta / +1 agilidade / +1 dano corpo a corpo)'.format(tri_esc))
                        
                        if tri_esc == 'Lutador':
                            
                            print ('Classe: Combatente / Subclasse: Atirador (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 luta / +1 agilidade / +1 forca)'.format(tri_esc))
                        
                        if tri_esc == 'Biologo':
                            
                            print ('Classe: Combatente / Subclasse: Atirador (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 ciencia / +1 adestramento)'.format(tri_esc))
                            
                        if tri_esc == 'Perito':
                            
                            print ('Classe: Combatente / Subclasse: Atirador (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+1 pericia / +1 investigacao / +1 percepcao \n +1 labia / +1 psicologia)'.format(tri_esc))

                        if tri_esc == 'T.I.':
                            
                            print ('Classe: Combatente / Subclasse: Atirador (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 tecnologia / +1 mecanica / +1 investigacao)'.format(tri_esc))
                            
                        if tri_esc == 'Mago Natural':
                            
                            print ('Classe: Combatente / Subclasse: Atirador (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos ocultos / +1 ciencias / +1 resistencia sanidade - paranormal)'.format(tri_esc))
                            
                        if tri_esc == 'Mago Psiquico':
                            
                            print ('Classe: Combatente / Subclasse: Atirador (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos oculto / +1 psicologia / +1 labia \n +1 resistencia sanidade - paranormal)'.format(tri_esc))
                        
                        if tri_esc == 'Necromante':
                            
                            print ('Classe: Combatente / Subclasse: Atirador (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos ocultos / +1 ciencias - morte / +1 resistencia sanidade - paranormal)'.format(tri_esc))
                                                                                               
                if esco_subc == 'Mercenario':
                    with open ('subclass_tri-mercenario.txt', 'r') as tri_merc:
                        tri_list = tri_merc.readlines()
                        tri_esc = random.choice(tri_list)
                        
                        if tri_esc == 'Atirador':

                            print ('Classe: Combatente / SubClasse: {} (+3 força / +2 luta / +1 agilidade / +2 dano corpo a corpo) / Trilha de SubClasse {} (+1 descricao / +1 perccepcao / +1 tiro)'.format(esco_subc, tri_esc))
                        
                        if tri_esc == 'Lutador':
                            
                            print ('Classe: Combatente / SubClasse: {} (+3 força / +2 luta / +1 agilidade / +2 dano corpo a corpo) / Trilha de SubClasse {} (+2 luta / +1 agilidade / +1 forca)'.format(esco_subc, tri_esc))
                
                        if tri_esc == 'Biologo':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 ciencia / +1 adestramento)'.format(esco_subc, tri_esc))
                            
                        if tri_esc == 'Perito':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+1 pericia / +1 investigacao / +1 percepcao \n +1 labia / +1 psicologia)'.format(esco_subc, tri_esc))

                        if tri_esc == 'T.I.':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 tecnologia / +1 mecanica / +1 investigacao)'.format(esco_subc, tri_esc))
                            
                        if tri_esc == 'Mago Natural':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos ocultos / +1 ciencias / +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                            
                        if tri_esc == 'Mago Psiquico':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos oculto / +1 psicologia / +1 labia \n +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                        
                        if tri_esc == 'Necromante':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos ocultos / +1 ciencias - morte / +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                                    
                if esco_subc == 'Lutador':
                    with open ('subclass_tri-lutador.txt', 'r') as tri_lut:
                        tri_list = tri_lut.readlines()
                        tri_esc = random.choice(tri_list)

                        if tri_esc == 'Mercenario':
                        
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 forca / +1 luta / +1 agilidade / +1 dano corpo a corpo)'.format(esco_subc, tri_esc))

                        if tri_esc == 'Atirador':

                            print ('Classe: Combatente / SubClasse: {} (+3 força / +2 luta / +1 agilidade / +2 dano corpo a corpo) / Trilha de SubClasse {} (+1 descricao / +1 perccepcao / +1 tiro)'.format(esco_subc, tri_esc))
                        
                        if tri_esc == 'Biologo':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 ciencia / +1 adestramento)'.format(esco_subc, tri_esc))
                            
                        if tri_esc == 'Perito':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+1 pericia / +1 investigacao / +1 percepcao \n +1 labia / +1 psicologia)'.format(esco_subc, tri_esc))

                        if tri_esc == 'T.I.':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 tecnologia / +1 mecanica / +1 investigacao)'.format(esco_subc, tri_esc))
                            
                        if tri_esc == 'Mago Natural':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos ocultos / +1 ciencias / +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                            
                        if tri_esc == 'Mago Psiquico':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos oculto / +1 psicologia / +1 labia \n +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                        
                        if tri_esc == 'Necromante':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos ocultos / +1 ciencias - morte / +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                                        
        if esc == 'Especialista':
            
            with open ('subclasss_esp.txt', 'r') as subesp:
                sub_esp_list = subesp.readlines()
                esco_subc = random.choice(sub_esp_list)
        
                if esco_subc == 'Biologo':
                    with open ('subclass_tri-biologo.txt', 'r') as tri_bio:
                        tri_list = tri_bio.readlines()
                        tri_esc = random.choice(tri_list)
                    
                        if tri_esc == 'Mercenario':
                        
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 forca / +1 luta / +1 agilidade / +1 dano corpo a corpo)'.format(esco_subc, tri_esc))

                        if tri_esc == 'Lutador':
                            
                            print ('Classe: Combatente / SubClasse: {} (+3 força / +2 luta / +1 agilidade / +2 dano corpo a corpo) / Trilha de SubClasse {} (+2 luta / +1 agilidade / +1 forca)'.format(esco_subc, tri_esc))
                        
                        if tri_esc == 'Atirador':

                            print ('Classe: Combatente / SubClasse: {} (+3 força / +2 luta / +1 agilidade / +2 dano corpo a corpo) / Trilha de SubClasse {} (+1 descricao / +1 perccepcao / +1 tiro)'.format(esco_subc, tri_esc))
                        
                        if tri_esc == 'Perito':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+1 pericia / +1 investigacao / +1 percepcao \n +1 labia / +1 psicologia)'.format(esco_subc, tri_esc))

                        if tri_esc == 'T.I.':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 tecnologia / +1 mecanica / +1 investigacao)'.format(esco_subc, tri_esc))
                            
                        if tri_esc == 'Mago Natural':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos ocultos / +1 ciencias / +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                            
                        if tri_esc == 'Mago Psiquico':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos oculto / +1 psicologia / +1 labia \n +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                        
                        if tri_esc == 'Necromante':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos ocultos / +1 ciencias - morte / +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                    
                if esco_subc == 'Perito':
                
                    with open ('subclass_tri-perito.txt', 'r') as tri_per:
                        tri_list = tri_per.readlines()
                        tri_esc = random.choice(tri_list)
                        
                        if tri_esc == 'Mercenario':
                        
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 forca / +1 luta / +1 agilidade / +1 dano corpo a corpo)'.format(esco_subc, tri_esc))
                        
                        if tri_esc == 'Lutador':
                            
                            print ('Classe: Combatente / SubClasse: {} (+3 força / +2 luta / +1 agilidade / +2 dano corpo a corpo) / Trilha de SubClasse {} (+2 luta / +1 agilidade / +1 forca)'.format(esco_subc, tri_esc))

                        if tri_esc == 'Atirador':

                            print ('Classe: Combatente / SubClasse: {} (+3 força / +2 luta / +1 agilidade / +2 dano corpo a corpo) / Trilha de SubClasse {} (+1 descricao / +1 perccepcao / +1 tiro)'.format(esco_subc, tri_esc))
                        
                        if tri_esc == 'Biologo':
                            
                                print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 ciencia / +1 adestramento)'.format(esco_subc, tri_esc))
                                
                        if tri_esc == 'T.I.':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 tecnologia / +1 mecanica / +1 investigacao)'.format(esco_subc, tri_esc))
                            
                        if tri_esc == 'Mago Natural':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos ocultos / +1 ciencias / +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                            
                        if tri_esc == 'Mago Psiquico':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos oculto / +1 psicologia / +1 labia \n +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                        
                        if tri_esc == 'Necromante':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos ocultos / +1 ciencias - morte / +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))

                if esco_subc == 'TI':
                    
                    with open ('subclass_tri-ti.txt', 'r') as tri_ti:
                        tri_list = tri_ti.readlines()
                        tri_esc = random.choice(tri_list)
                        
                        if tri_esc == 'Mercenario':
                        
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 forca / +1 luta / +1 agilidade / +1 dano corpo a corpo)'.format(esco_subc, tri_esc))
                        
                        if tri_esc == 'Lutador':
                            
                            print ('Classe: Combatente / SubClasse: {} (+3 força / +2 luta / +1 agilidade / +2 dano corpo a corpo) / Trilha de SubClasse {} (+2 luta / +1 agilidade / +1 forca)'.format(esco_subc, tri_esc))

                        if tri_esc == 'Atirador':

                            print ('Classe: Combatente / SubClasse: {} (+3 força / +2 luta / +1 agilidade / +2 dano corpo a corpo) / Trilha de SubClasse {} (+1 descricao / +1 perccepcao / +1 tiro)'.format(esco_subc, tri_esc))
                        
                        if tri_esc == 'Biologo':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 ciencia / +1 adestramento)'.format(esco_subc, tri_esc))
                            
                        if tri_esc == 'Perito':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+1 pericia / +1 investigacao / +1 percepcao \n +1 labia / +1 psicologia)'.format(esco_subc, tri_esc))
                            
                        if tri_esc == 'Mago Natural':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos ocultos / +1 ciencias / +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                            
                        if tri_esc == 'Mago Psiquico':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos oculto / +1 psicologia / +1 labia \n +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                        
                        if tri_esc == 'Necromante':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos ocultos / +1 ciencias - morte / +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                 
        if esc == 'Ocultista':
            
            with open ('subclass_ocul.txt', 'r') as subocul:
                sub_ocul_list = subocul.readlines()
                esco_subc = random.choice(sub_ocul_list)
                
                if esco_subc == 'Necromante':
                    
                    with open ('ritu_necro.txt', 'r') as ritu_necro:
                        
                        ritu_necro_list = ritu_necro.readlines()
                        ritu_necro_esc = random.choice(ritu_necro_list)
                        print ('Classe: Ocultista / SubClasse: {} (+3 estudos ocultos / +2 ciencias - morte \n +2 resistencia sanidade - paranormal \n Ritual: {})'.format(esco_subc, ritu_necro_esc))
                        
                        with open ('subclass_tri-necromante.txt', 'r') as tri_necro:
                            tri_list = tri_necro.readlines()
                            tri_esc = random.choice(tri_list)
                        
                            if tri_esc == 'Mercenario':
                        
                                print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 forca / +1 luta / +1 agilidade / +1 dano corpo a corpo)'.format(esco_subc, tri_esc))
                            
                            if tri_esc == 'Lutador':
                            
                                print ('Classe: Combatente / SubClasse: {} (+3 força / +2 luta / +1 agilidade / +2 dano corpo a corpo) / Trilha de SubClasse {} (+2 luta / +1 agilidade / +1 forca)'.format(esco_subc, tri_esc))

                            if tri_esc == 'Atirador':

                                print ('Classe: Combatente / SubClasse: {} (+3 força / +2 luta / +1 agilidade / +2 dano corpo a corpo) / Trilha de SubClasse {} (+1 descricao / +1 perccepcao / +1 tiro)'.format(esco_subc, tri_esc))
                        
                            if tri_esc == 'Biologo':
                            
                                print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 ciencia / +1 adestramento)'.format(esco_subc, tri_esc))
                            
                            if tri_esc == 'Perito':
                            
                                print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+1 pericia / +1 investigacao / +1 percepcao \n +1 labia / +1 psicologia)'.format(esco_subc, tri_esc))

                            if tri_esc == 'T.I.':
                            
                                print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 tecnologia / +1 mecanica / +1 investigacao)'.format(esco_subc, tri_esc))
                            
                            if tri_esc == 'Mago Natural':
                            
                                print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos ocultos / +1 ciencias / +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                            
                            if tri_esc == 'Mago Psiquico':
                            
                                print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos oculto / +1 psicologia / +1 labia \n +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                    
                if esco_subc == 'Mago Natural':
                    
                    with open ('ritu_nat.txt', 'r') as ritu_nat:
                        
                        ritu_nat_list = ritu_nat.readlines()
                        ritu_nat_esc = random.choice(ritu_nat_list)
                        print ('Classe: Ocultista / SubClasse: {} (+3 estudos ocultos / +2 ciencias / +2 resistencia sanidade - paranormal \n Ritual: {})'.format(esco_subc, ritu_nat_esc))
                    
                        with open ('subclass_tri-mago_nat.txt', 'r') as tri_nat:
                        
                            tri_list = tri_nat.readlines()
                            tri_esc = random.choice(tri_list)
                
                            if tri_esc == 'Mercenario':
                        
                                print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 forca / +1 luta / +1 agilidade / +1 dano corpo a corpo)'.format(esco_subc, tri_esc))
                        
                            if tri_esc == 'Lutador':
                            
                                print ('Classe: Combatente / SubClasse: {} (+3 força / +2 luta / +1 agilidade / +2 dano corpo a corpo) / Trilha de SubClasse {} (+2 luta / +1 agilidade / +1 forca)'.format(esco_subc, tri_esc))

                            if tri_esc == 'Atirador':

                                print ('Classe: Combatente / SubClasse: {} (+3 força / +2 luta / +1 agilidade / +2 dano corpo a corpo) / Trilha de SubClasse {} (+1 descricao / +1 perccepcao / +1 tiro)'.format(esco_subc, tri_esc))
                        
                            if tri_esc == 'Biologo':
                            
                                print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 ciencia / +1 adestramento)'.format(esco_subc, tri_esc))
                            
                            if tri_esc == 'Perito':
                            
                                print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+1 pericia / +1 investigacao / +1 percepcao \n +1 labia / +1 psicologia)'.format(esco_subc, tri_esc))

                            if tri_esc == 'T.I.':
                            
                                print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 tecnologia / +1 mecanica / +1 investigacao)'.format(esco_subc, tri_esc))
                            
                            if tri_esc == 'Mago Psiquico':
                            
                                print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos oculto / +1 psicologia / +1 labia \n +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                        
                            if tri_esc == 'Necromante':
                            
                                print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos ocultos / +1 ciencias - morte / +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                
                if esco_subc == 'Mago Psiquico':
                    
                    with open ('ritu_psi.txt', 'r') as ritu_psi:
                        
                        ritu_psi_list = ritu_psi.readlines()
                        ritu_psi_esc = random.choice(ritu_psi_list)
                        print ('Classe: Ocultista / SubClasse: {} (+3 estudos ocultos / +2 psicologia / +2 labia / +2 resistencia sanidade - paranormal \n Ritual: {})'.format(esco_subc, ritu_psi_esc))

                        with open ('subclass_tri-mago_psi.txt', 'r') as tri_psi:
                        
                            tri_list = tri_psi.readlines()
                            tri_esc = random.choice(tri_list)
                        
                        if tri_esc == 'Mercenario':
                        
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 forca / +1 luta / +1 agilidade / +1 dano corpo a corpo)'.format(esco_subc, tri_esc))
                            
                        if tri_esc == 'Lutador':
                            
                            print ('Classe: Combatente / SubClasse: {} (+3 força / +2 luta / +1 agilidade / +2 dano corpo a corpo) / Trilha de SubClasse {} (+2 luta / +1 agilidade / +1 forca)'.format(esco_subc, tri_esc))

                        if tri_esc == 'Atirador':

                            print ('Classe: Combatente / SubClasse: {} (+3 força / +2 luta / +1 agilidade / +2 dano corpo a corpo) / Trilha de SubClasse {} (+1 descricao / +1 perccepcao / +1 tiro)'.format(esco_subc, tri_esc))
                        
                        if tri_esc == 'Biologo':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 ciencia / +1 adestramento)'.format(esco_subc, tri_esc))
                            
                        if tri_esc == 'Perito':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+1 pericia / +1 investigacao / +1 percepcao \n +1 labia / +1 psicologia)'.format(esco_subc, tri_esc))

                        if tri_esc == 'T.I.':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 tecnologia / +1 mecanica / +1 investigacao)'.format(esco_subc, tri_esc))
                            
                        if tri_esc == 'Mago Natural':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos ocultos / +1 ciencias / +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
                            
                        if tri_esc == 'Necromante':
                            
                            print ('Classe: Combatente / Subclasse: {} (+1 discrição / +2 perícia / +2 tiro \n Trilha de Subclasse: {} (+2 estudos ocultos / +1 ciencias - morte / +1 resistencia sanidade - paranormal)'.format(esco_subc, tri_esc))
