import csv

def generate(input_csv, output_cbi):
    with open(input_csv, newline='', encoding='utf-8') as csvfile, open(output_cbi, 'w', encoding='utf-8') as cbifile:
        reader = csv.DictReader(csvfile, delimiter=';')

        # Record di testa
        record_pc = f"PC{'0'*5}00123{'070123':<6}{'NOMESUPPORTO':<20}{' ':<61}E{' ':<5}\n"
        cbifile.write(record_pc)

        total_dispositions = 0
        total_amount = 0
        record_count = 1

        for row in reader:
            print(reader.fieldnames)
            print(row)
            # print(row['execution_date'])
            # exit()

            # Record "10"
            total_dispositions += 1
            amount_cents = int(float(row["amount"]) * 100)
            total_amount += amount_cents
            record_10 = (
                f"10{record_count:06d}{' ':<11}"
                f"{row['execution_date']:<6}"
                f"{row['value_date']:<6}"
                f"{row['causal']:<5}"
                f"{amount_cents:012d}+"
                f"{row['bank_code']:<5}"
                f"{row['cab_code']:<5}"
                f"{row['account']:<12}"
                f"{row['dest_bank']:<5}"
                f"{row['dest_cab']:<5}"
                f"{row['dest_account']:<12}"
                f"{' ':<30}E\n"
            )
            cbifile.write(record_10)

            # Record "20" (Descrizione dell'azienda ordinante)
            record_20 = (
                f"20{record_count:06d}"
                f"{row['company_name']:<30}"
                f"{row['company_address']:<30}"
                f"{row['company_city']:<30}"
                f"{row['company_tax_code']:<16}"
                f"{' ':<4}\n"
            )
            cbifile.write(record_20)

            # Record "30" (Descrizione del cliente destinatario)
            record_30 = (
                f"30{record_count:06d}"
                f"{row['dest_name']:<30}"
                f"{row['dest_address']:<30}"
                f"{row['dest_city']:<30}"
                f"{row['dest_tax_code']:<16}"
                f"{' ':<4}\n"
            )
            cbifile.write(record_30)

            # Record "40" (Indirizzo del cliente destinatario)
            record_40 = (
                f"40{record_count:06d}"
                f"{row['dest_address']:<30}"
                f"{row['dest_zip']:<5}"
                f"{row['dest_city']:<25}"
                f"{row['dest_bank_name']:<50}\n"
            )
            cbifile.write(record_40)

            # Record "50" (Descrizione ad uso del cliente destinatario)
            description = row['description']
            record_50 = (
                f"50{record_count:06d}"
                f"{description[:30]:<30}"
                f"{description[30:60]:<30}"
                f"{description[60:90]:<30}"
                f"{' ':<20}\n"
            )
            cbifile.write(record_50)

            # Record "70" (Qualificatore flusso e chiavi di controllo)
            record_70 = (
                f"70{record_count:06d}"
                f"{' ':<25}"  # Blank filler
                f"{'1':<1}"   # Tipo flusso
                f"{'$':<1}"   # Qualificatore flusso
                f"{row['gateway_abi']:<5}"  # Soggetto veicolatore
                f"{row['mp_code']:<5}"     # Codice MP
                f"{' ':<27}"  # Blank filler
                f"{'1':<1}"   # Flag richiesta
                f"{row['unique_code']:<30}"  # Codice univoco
                f"{' ':<10}"  # Filler
                f"E\n"
            )
            cbifile.write(record_70)

            record_count += 1

        # Record di coda
        record_ef = (
            f"EF{'0'*5}00123{'070123':<6}{'NOMESUPPORTO':<20}"
            f"{total_dispositions:06d}"
            f"{total_amount:015d}"
            f"{record_count:06d}"
            f"{' ':<24}E\n"
        )
        cbifile.write(record_ef)

def genera(input_csv, output_cbi):
    with open(input_csv, newline='', encoding='utf-8') as csvfile, open(output_cbi, 'w', encoding='utf-8') as cbifile:
        reader = csv.DictReader(csvfile, delimiter=";")

        # Record di testa
        record_pc = f"PC{'0'*5}00123{'070123':<6}{'NOMEFLUSSO':<20}{' ':<61}E{' ':<5}\n"
        cbifile.write(record_pc)

        numero_disposizioni = 0
        importo_totale = 0
        numero_record = 1

        for riga in reader:
            # Record "10"
            numero_disposizioni += 1
            importo_cent = int(float(riga["importo"]) * 100)
            importo_totale += importo_cent
            record_10 = (
                f"10{numero_record:06d}{' ':<11}"
                f"{riga['data_esecuzione']:<6}"
                f"{riga['data_valuta']:<6}"
                f"{riga['causale']:<5}"
                f"{importo_cent:012d}+"
                f"{riga['banca_ordinante_abi']:<5}"
                f"{riga['cab_ordinante']:<5}"
                f"{riga['conto_ordinante']:<12}"
                f"{riga['banca_destinataria_abi']:<5}"
                f"{riga['cab_destinataria']:<5}"
                f"{riga['conto_destinatario']:<12}"
                f"{' ':<30}E\n"
            )
            cbifile.write(record_10)

            # Record "16" (IBAN Ordinante)
            if riga["iban_ordinante"]:
                iban = riga["iban_ordinante"]
                record_16 = (
                    f"16{numero_record:06d}"
                    f"{iban[:2]:<2}"        # Codice Paese
                    f"{iban[2:4]:<2}"      # Check Digit
                    f"{iban[4:5]:<1}"      # CIN
                    f"{iban[5:10]:<5}"     # ABI
                    f"{iban[10:15]:<5}"    # CAB
                    f"{iban[15:27]:<12}"   # Numero Conto
                    f"{' ':<83}\n"
                )
                cbifile.write(record_16)

            # Record "17" (IBAN Beneficiario)
            if riga["iban_destinatario"]:
                iban = riga["iban_destinatario"]
                record_17 = (
                    f"17{numero_record:06d}"
                    f"{iban[:2]:<2}"        # Codice Paese
                    f"{iban[2:4]:<2}"      # Check Digit
                    f"{iban[4:5]:<1}"      # CIN
                    f"{iban[5:10]:<5}"     # ABI
                    f"{iban[10:15]:<5}"    # CAB
                    f"{iban[15:27]:<12}"   # Numero Conto
                    f"{' ':<83}\n"
                )
                cbifile.write(record_17)

            # Record "20" (Dati ordinante)
            record_20 = (
                f"20{numero_record:06d}"
                f"{riga['ragione_sociale_ordinante']:<30}"
                f"{riga['indirizzo_ordinante']:<30}"
                f"{riga['localita_ordinante']:<30}"
                f"{riga['codice_fiscale_ordinante']:<16}"
                f"{' ':<4}\n"
            )
            cbifile.write(record_20)

            # Record "30" (Dati destinatario)
            record_30 = (
                f"30{numero_record:06d}"
                f"{riga['ragione_sociale_destinatario']:<30}"
                f"{riga['indirizzo_destinatario']:<30}"
                f"{riga['localita_destinatario']:<30}"
                f"{riga['codice_fiscale_destinatario']:<16}"
                f"{' ':<4}\n"
            )
            cbifile.write(record_30)

            # Record "40" (Indirizzo destinatario)
            record_40 = (
                f"40{numero_record:06d}"
                f"{riga['indirizzo_destinatario']:<30}"
                f"{riga['cap_destinatario']:<5}"
                f"{riga['localita_destinatario']:<25}"
                f"{riga['banca_destinataria_nome']:<50}\n"
            )
            cbifile.write(record_40)

            # Record "50" (Descrizione pagamento)
            descrizione = riga['descrizione']
            record_50 = (
                f"50{numero_record:06d}"
                f"{descrizione[:30]:<30}"
                f"{descrizione[30:60]:<30}"
                f"{descrizione[60:90]:<30}"
                f"{' ':<20}\n"
            )
            cbifile.write(record_50)

            # Record "70" (Qualificatore e controlli)
            record_70 = (
                f"70{numero_record:06d}"
                f"{' ':<25}"  # Blank filler
                f"{'1':<1}"   # Tipo flusso
                f"{'$':<1}"   # Qualificatore flusso
                f"{riga['abi_gateway']:<5}"  # Soggetto veicolatore
                f"{riga['codice_mp']:<5}"     # Codice MP
                f"{' ':<27}"  # Blank filler
                f"{'1':<1}"   # Flag richiesta
                f"{riga['codice_univoco']:<30}"  # Codice univoco
                f"{' ':<10}"  # Filler
                f"E\n"
            )
            cbifile.write(record_70)

            numero_record += 1

        # Record di coda
        record_ef = (
            f"EF{'0'*5}00123{'070123':<6}{'NOMEFLUSSO':<20}"
            f"{numero_disposizioni:06d}"
            f"{importo_totale:015d}"
            f"{numero_record:06d}"
            f"{' ':<24}E\n"
        )
        cbifile.write(record_ef)

# Esempio di uso
#genera_cbi("input_dati.csv", "output_flusso.cbi")

''' csv di esempio
data_esecuzione;data_valuta;causale;importo;banca_ordinante_abi;cab_ordinante;conto_ordinante;banca_destinataria_abi;cab_destinataria;conto_destinatario;iban_ordinante;iban_destinatario;ragione_sociale_ordinante;indirizzo_ordinante;localita_ordinante;codice_fiscale_ordinante;ragione_sociale_destinatario;indirizzo_destinatario;localita_destinatario;codice_fiscale_destinatario;cap_destinatario;banca_destinataria_nome;descrizione;abi_gateway;codice_mp;codice_univoco
23122024;24122024;48000;100.50;1100;12345;678900;3262;54321;9876543210;IT60X0542811101000000123456;IT60X0542811101000000654321;Azienda S.p.A.;Via Roma 10;Roma;12345678901;Cliente S.r.l.;Via Milano 20;Milano;98765432109;20100;Banca Milano;Pagamento ordine;3262;54321;11223344
'''

import csv

def cbi_to_csv(input_cbi, output_csv):
    # TODO: aggiungere ciclo per numero_disposizione (altrimenti non funziona)
    with open(input_cbi, 'r', encoding='utf-8') as cbifile, open(output_csv, 'a', newline='', encoding='utf-8') as csvfile:
        # Nomi delle colonne per il CSV
        fieldnames = [
            "numero_disposizione", "data_esecuzione", "data_valuta", "causale", "importo", "banca_ordinante_abi", "cab_ordinante",
            "conto_ordinante", "banca_destinataria_abi", "cab_destinataria", "conto_destinatario",
            "iban_ordinante", "iban_destinatario", "ragione_sociale_ordinante", "indirizzo_ordinante",
            "localita_ordinante", "codice_fiscale_ordinante", "ragione_sociale_destinatario",
            "indirizzo_destinatario", "localita_destinatario", "codice_fiscale_destinatario",
            "cap_destinatario", "banca_destinataria_nome", "descrizione", "abi_gateway", "codice_mp",
            "codice_univoco"
        ]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        current_row = {
            field: "" for field in fieldnames  # Inizializza una riga vuota
        }

        for line in cbifile:
            record_type = line[1:3]  # Tipo di record (es. "10", "16")

            if record_type == "10":
                current_row = {field: "" for field in fieldnames}  # Reset della riga
                current_row["numero_disposizione"] = line[3:9].strip()
                current_row["data_esecuzione"] = line[16:22].strip()
                current_row["data_valuta"] = line[23:29].strip()
                current_row["causale"] = line[28:34].strip()
                current_row["importo"] = str(int(line[34:46].strip()) / 100)  # Cent in euro
                current_row["banca_ordinante_abi"] = line[48:53].strip()
                current_row["cab_ordinante"] = line[53:58].strip()
                current_row["conto_ordinante"] = line[58:70].strip()
                current_row["banca_destinataria_abi"] = line[70:75].strip()
                current_row["cab_destinataria"] = line[75:80].strip()
                current_row["conto_destinatario"] = line[80:92].strip()

            elif record_type == "16":
                current_row["iban_ordinante"] = (
                    line[11:13].strip() + line[13:15].strip() + line[15:16].strip() +
                    line[16:21].strip() + line[21:26].strip() + line[26:38].strip()
                )

            elif record_type == "17":
                current_row["iban_destinatario"] = (
                    line[11:13].strip() + line[13:15].strip() + line[15:16].strip() +
                    line[16:21].strip() + line[21:26].strip() + line[26:38].strip()
                )

            elif record_type == "20":
                current_row["ragione_sociale_ordinante"] = line[11:41].strip()
                current_row["indirizzo_ordinante"] = line[41:71].strip()
                current_row["localita_ordinante"] = line[71:101].strip()
                current_row["codice_fiscale_ordinante"] = line[101:117].strip()

            elif record_type == "30":
                current_row["ragione_sociale_destinatario"] = "BENEFICIARIO GENERICO"  # Nome generico per privacy
                current_row["indirizzo_destinatario"] = line[41:71].strip()
                current_row["localita_destinatario"] = line[71:101].strip()
                current_row["codice_fiscale_destinatario"] = line[101:117].strip()

            elif record_type == "40":
                current_row["cap_destinatario"] = line[41:46].strip()
                current_row["banca_destinataria_nome"] = line[71:121].strip()

            elif record_type == "50":
                descrizione = current_row.get("descrizione", "")
                current_row["descrizione"] = descrizione + line[11:101].strip()

            elif record_type == "70":
                current_row["abi_gateway"] = line[33:38].strip()
                current_row["codice_mp"] = line[38:43].strip()
                current_row["codice_univoco"] = line[71:101].strip()

            elif record_type == "EF":
                # Fine della disposizione, scrivi la riga nel CSV
                writer.writerow(current_row)


if __name__ == "__main__":
    path_file = './data/'
    path_file_in = './data/cbi_input.csv'
    path_file_out = './data/cbi_output.cbi'
    path_file_in_it = './data/cbi_input_it.csv'
    path_file_out_it = './data/cbi_output_it.cbi'

    # generate(path_file_in, path_file_out)
    # genera(path_file_in_it, path_file_out_it)

    cbi_to_csv(path_file + "CBI_1227.sti", path_file + "cbi_output_1227.csv")
