# Scanvox pro NVDA

* Autor: Nael Sayegh
* e-mailová adresa: [infos@nael-accessvision.com](mailto:infos@nael-accessvision.com)
* Stáhnout [Stabilní verzi][1];
*Kompatibilní verze NVDA : 2021.3 a novější;
* [Zdrojový kód na GitHubU][2];

# Popis

Tento doplněk využívá Scanvox software pro skenování dokumentů ze skeneru s rozhraním Twain a Wia. Program byl vytvořen s pomocí vývojáře softwaru Scanvox, nevyžaduje se žádná speciální instalace, pouze ovladače ke skeneru.

## Požadavky 

Doplněk vyžaduje USB skener připojený k počítači  a nainstalované ovladače, program umí skenovat přes TWAIN nebo WIA rozhraní, která se používají s většinou skenerů.

## Použití doplňku

Doplněk se používá jednoduše stiskněte nvdaklávesu +n, najděte položku ScanVox. Zde je tlačítko skenovat a editační pole jen pro čtení, do kterého přibývá naskenovaný text. po stisknutí enteru začne skenování a poté se začne automaticky číst text. Můžete naskenovat i více stránek a poté text uložit do formátu Word .docx nebo txt souboru. Pokud text neuložíte, text se po uzavření okna vymaže.

### Klávesové zkratky

Doplněk lze spustit kdekoli klávesovou zkratkou inzert +alt +s.

## Změny

### Verze 2024.05.07

  * Přidána možnost výběru aktualizace z vývojového kanálu
  * Přidán turecký překlad
  * Při uložení do dokumentu aplikace Word se každá naskenovaná stránka uloží na novou samostatnou stránku v souboru
  * Do výpisu logu v NVDA přidána informace, že ScanVox je spuštěn

### Verze 2024.05.04

  * Vylepšení systému aktualizací
  * Aktualizace ruského překladu
  * Oprava francouzského překladu
  * Opravena chyba, kdy po stisku tlačítka smazat nebyl smazán obsah oblasti pro editaci
  * Automatické umístění kurzoru na začátek skenované stránky v oblasti pro editaci.
  * Přidání čísla stránky na vrch každé skenované stránky v oblasti pro editaci
  * Přesun menu Scanvox z nástrojového menu do hlavního menu

### Verze 2024.03.20

  * Přidán český překlad včetně dokumentace
  *  Přidán Portugalský překlad
  *  Přidáno víceřádkové editační pole jen pro čtení před tlačítko skenovat, zde je možné číst již naskenovaný text
  *Přidána možnost zapnout / vypnout automatické čtení textu po skenování jde nastavit v nastavení  NVDA / kategorie Scanvox
  * Přidán ruský překlad

### Verze 2024.01.10

  *Přidáno tlačítko co je nového
Nové funkce
  *Podpora automatického čtení dokumentu po skenování
  *Přidán oddělovač hvězdička do souboru

### Verze 2024.01.03

  * Aktualizovaná Francouzská nápověda

### Verze 2023.12.29

  * První verze

[1]: https://github.com/Nael-Sayegh/scanvox-for-nvda/releases/download/2024.05.04/scanvox-2024.05.04.nvda-addon

[2]: https://github.com/Nael-Sayegh/scanvox-for-nvda
