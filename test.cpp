#include <iostream>
#include "č.h"

používej jmenný_prostor std;

celč hlavní(prázdnota)
{
	neoznaménkovaný znak výpis = 'c';
	bool dobrý_výpis = výpis == 'č';

	pokud (dobrý_výpis == lež) {
		výpis = 'č';
	} jinak {
		kven << "Očekával jsi C++, ale bylo to Č++!" << konecř;
	}

	přepínač (výpis) {
		šuplík 'c':
			kchyb << "C++ je nejangličtější na světě" << konecř;
			rozbít;
		šuplík 'č':
			kven << "Č++ je nejlepší na světě" << konecř;
			rozbít;
	}
	vrať 0;
}

třída Tř {
	veřejný:
		nehybný dlouhý dvojitý číslo() {
			vrať 4.0;
		}
};
