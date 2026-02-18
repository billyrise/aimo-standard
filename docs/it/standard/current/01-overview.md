---
description: Panoramica di AIMO Standard. Definisce tassonomia condivisa, sistema di codici, dizionario, modelli di evidenza e controlli del Validator per audit di governance IA.
---
<!-- aimo:translation_status=translated -->

# Panoramica（Overview）

**AIMO** sta per **AI Management Office**. AIMO Standard definisce:
- una tassonomia condivisa
- un sistema di codici
- un dizionario iniziale
- un modello EV
- controlli del Validator (specifica + implementazione di riferimento minima)

Questo repository pubblica:
- specifica leggibile (HTML)
- artefatti leggibili da macchina (schemi/modelli/esempi)
- release PDF ufficiali

## Posizionamento: complemento a ISO/IEC 42001 (AIMS)

AIMO Standard è un **acceleratore di implementazione per preparazione delle evidenze e spiegabilità**, utilizzabile per supportare Sistemi di Gestione IA (AIMS) allineati a ISO/IEC 42001 e per strutturare evidenze pronte per l’audit. Non sostituisce ISO/IEC 42001 né altre norme di sistemi di gestione; aggiunge tassonomia, struttura Evidence Bundle e Coverage Map che aiutano a operativizzare e documentare quei controlli.

**Cosa fornisce AIMO**

- Tassonomia e sistema di codici per la classificazione della governance IA
- Struttura Evidence Bundle (manifest, object_index, payload_index, integrità)
- Validator e Coverage Map per la tracciabilità
- Livelli di conformità (Foundation, Operational, Audit-Ready) — livelli di maturità solo AIMO per il confezionamento delle evidenze

**Cosa non fornisce AIMO**

- Consulenza legale
- Certificazione ISO o sostituto della certificazione
- Garanzia di conformità normativa
- Sostituto del giudizio dell’auditor o degli organismi di certificazione accreditati

**Perché ora**

- **ISO/IEC 42006** (pubblicata luglio 2025) specifica i requisiti per gli organismi che verificano e certificano i sistemi di gestione IA secondo ISO/IEC 42001, aumentando le aspettative su evidenze verificabili e tracciabilità.
- L’**EU AI Act** è in applicazione progressiva (2025–2027); le norme armonizzate, una volta pubblicate nella Gazzetta ufficiale, forniranno presunzione di conformità. L’EU AI Office sta preparando linee guida pratiche nel 2026 (classificazione ad alto rischio, trasparenza Art. 50, incidenti, elementi QMS).
- Adottanti e organismi di certificazione usano sempre più ISO/IEC 42001 come livello di sistema per la governance IA; AIMO aiuta a strutturare evidenze che supportano quel livello senza rivendicare certificazione.

## Riferimenti

- [ISO/IEC 42006](https://www.iso.org/standard/42006) — Requisiti per organismi che verificano e certificano sistemi di gestione IA
- [Calendario di applicazione EU AI Act](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act) (Servizio Legge sull'IA della Commissione europea; informativo)
- [European Commission — Clear guidelines for AI (4 dic 2025)](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_xxxx) — Preparazione linee guida AI Office (verificare notizie Commissione per URL attuale)
- [EPRS — EU AI Act implementation timeline (giu 2025)](https://www.europarl.europa.eu/thinktank/en/document/EPRS_BRI) — Briefing Parlamento (informativo)
