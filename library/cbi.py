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

if __name__ == "__main__":
    path_file_in = './data/input.csv'
    path_file_out = './data/output.cbi'

    generate(path_file_in, path_file_out)
    
    # Esempio di uso
    # generate("input.csv", "output.cbi")
