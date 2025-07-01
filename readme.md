# Scanvox for NVDA

* Author: Nael Sayegh
* URL: [infos@nael-accessvision.com](mailto:infos@nael-accessvision.com)
* Download the [stable version][1];
* NVDA Compatibility: 2021.3 and above;
* [Source code on GitHub][2];

# Presentation

This add-on uses the Scanvox software to read your paper documents. It was created with the help of the software developer and does not require any additional installation.

## Prerequisites 

To use this add-on, you must have a USB scanner connected to your computer that is compatible with TWAIN or WIA, which is the case with most scanners.

## How it works

To use this add-on, go to the NVDA menu, then select Scanvox. In this dialog, you can start a scan by clicking on the Scan button. The scan takes a few seconds to start, and then, at the end of the scanning process, the scanned text is automatically read out loud. You can deactivate automatic playback by going to the NVDA settings menu, then to the scanvox for NVDA category. Press this button until all pages have been scanned. If you want to delete the page you just scanned, you can press the "delete last scanned page" button next to the scanned button with tabulation or by using the shortcut alt+l. Once finished, you can read the different scanned pages by doing shift+tab from the scanned button or by doing alt+t to access an editing area with the content of all the pages. In this edit area, if you want to move quickly from page to page, you can use the previous page and next page buttons, or use the shortcuts ctrl+shift+up arrow and ctrl+shift+down arrow. You can save the file using the corresponding button.
If you want to delete the scanned pages to scan a new document, you can press the button to cancel all scanned pages.
When you exit Scanvox, all scanned pages are erased.

### Keyboard Shortcuts

The add-on "Scanvox for NVDA" can be launched from anywhere on your computer by pressing nvda+alt+s. This gesture can be modified in the input gestures dialog.

## Changes

### Version 2025.07.01

  * Compatibility tested with NVDA 2025.1

### Version 2024.08.15

  * In the editing area, you can now use the previous and next page keys or ctrl+shift+up arrow and ctrl+shift+down arrow to quickly move from one page to another.
  * Adding a button to delete the last scanned page
  * Reversal of the file formats in the format list in the save file dialog. The default format is docx.
  * Modernization of the update system to use the GitHub API to check and install new versions. This also fixes the installation issue of dev versions.
  * Fix for the module loading issue that would freeze when no internet connection was detected.

### Version 2024.07.02

  * Fixed an issue where page numbers continued to increase after clicking delete.

### Version 2024.06.01

  * Addition of a dev update channel for translators and testing new features
  * Adding Turkish translation
  * When saving a Word document, each page is added as a new page in the file.
  * Adding a message in the NVDA log to indicate that Scanvox is loaded
  * Documentation updated

### Version 2024.05.04

  * Improvement of the update system
  * Updating the Russian translation
  * French translation correction
  * Fixed a bug that did not delete the content of the editing area when pressing the delete button
  * Automatically place the cursor at the beginning of the scanned page in the editing area.
  * Addition of page number at the top of each scanned page in the editing area
  * Moving the Scanvox menu from the tool menu to the main menu

### Version 2024.03.20

  * Addition of Czech translation
  * Addition of Portuguese translation
  * Addition of an editing area before the scan button allowing to immediately read the text that has just been scanned
  * Add a parameter to disable / enable automatic reading of a document, go to the NVDA settings menu then Scanvox for NVDA
  * Addition of Russian translation

### Version 2024.01.10

  * Update system modification to add a "What's New" button that opens the help with the new features of the version
  * Addition of automatic reading of the scanned page after scanning
  * Addition of a page separator in the file (20 asterisks) to indicate when the page changes

### Version 2024.01.03

  * Updated French Help

### Version 2023.12.29

  * First version

[1]: https://github.com/Nael-Sayegh/scanvox-for-nvda/releases/download/2025.07.01/scanvox-2025.07.01.nvda-addon

[2]: https://github.com/Nael-Sayegh/scanvox-for-nvda