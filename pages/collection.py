#!/usr/bin/env python

# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Selenium Tests.
#
# The Initial Developer of the Original Code is
# Mozilla.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Bebe <florin.strugariu@softvision.ro>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

from selenium.webdriver.common.by import By

from pages.base import Base


class Collections(Base):

    _page_title = "Featured Collections :: Add-ons for Firefox"

    #Search box
    _search_button_locator = (By.CSS_SELECTOR, "button.search-button")
    _search_textbox_locator = (By.NAME, "q")
    _collection_name = (By.CSS_SELECTOR, "h2.collection > span")

    @property
    def collection_name(self):
        return self.selenium.find_element(*self._collection_name).text

    def search_for(self, search_term):
        search_box = self.selenium.find_element(*self._search_textbox_locator)
        search_box.send_keys(search_term)
        self.selenium.find_element(*self._search_button_locator).click()
        return CollectionsSearch(self.testsetup)


class CollectionsSearch(Base):

    _results_locator = (By.CSS_SELECTOR, "div.featured-inner div.item")

    @property
    def result_count(self):
        return len(self.selenium.find_elements(*self._results_locator))
