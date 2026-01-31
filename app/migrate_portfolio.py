import csv
import os
from sqlalchemy.orm import Session
from app import db, models

CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "portfolio.csv")

def migrate():
    session: Session = db.SessionLocal()
    try:
        with open(CSV_PATH, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            print("Encabezados CSV detectados:", reader.fieldnames)

            for row in reader:
                ticker = row["ticker"].strip()
                quantity = float(row["quantity"].strip())
                
                # Asignamos price=0 si no existe columna
                price = float(row.get("price", 0))

                # Evita duplicados
                existing = session.query(models.Portfolio).filter_by(symbol=ticker).first()
                if existing:
                    existing.quantity = quantity
                    existing.avg_price = price
                    session.add(existing)
                else:
                    asset = models.Portfolio(
                        symbol=ticker,
                        quantity=quantity,
                        avg_price=price
                    )
                    session.add(asset)
        session.commit()
        print("Migración completada ✅")
    except Exception as e:
        print(f"Error en migración: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    migrate()
