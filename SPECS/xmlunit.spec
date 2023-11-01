# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Name:           xmlunit
Version:        1.6
Release:        7%{?dist}
Epoch:          0
Summary:        Provides classes to do asserts on xml
License:        BSD
Source0:        http://downloads.sourceforge.net/xmlunit/xmlunit-1.6-src.zip
Source1:        http://repo1.maven.org/maven2/xmlunit/xmlunit/1.0/xmlunit-1.0.pom
URL:            http://xmlunit.sourceforge.net/
BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  junit
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis

Requires:       junit
Requires:       xalan-j2
Requires:       xml-commons-apis

BuildArch:      noarch

%description
XMLUnit extends JUnit to simplify unit testing of XML. It compares a control
XML document to a test document or the result of a transformation, validates
documents against a DTD, and (from v0.5) compares the results of XPath
expressions.

%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
Javadoc for %{name}

%prep
%setup -q

sed -i /java.class.path/d build.xml
# remove all binary libs and javadocs
find . -name "*.jar" -exec rm -f {} \;
rm -rf doc

#Fix wrong-file-end-of-line-encoding
sed -i 's/\r//g' README.txt LICENSE.txt

%mvn_file : %{name}

%build
ant -Dbuild.compiler=modern -Dhaltonfailure=yes \
    -Djunit.lib=$(build-classpath junit) \
    -Dxmlxsl.lib= -Dtest.report.dir=test \
    -Ddb5.xsl=%{_datadir}/sgml/docbook/xsl-ns-stylesheets \
    jar javadocs

%mvn_artifact %{SOURCE1} build/lib/%{name}-%{version}.jar

%install
%mvn_install -J build/doc/api/

%check
ant


%files -f .mfiles
%doc README.txt LICENSE.txt userguide/XMLUnit-Java.pdf

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 01 2017 Michael Simacek <msimacek@redhat.com> - 0:1.6-5
- Install with XMvn

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan 04 2015 Dr. Tilmann Bubeck <tilmann@bubecks.de> - 0:1.6-1
- update to upstream's xmlunit-1.6

* Wed Nov  5 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.5-3
- Remove workaround for RPM bug #646523

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 11 2013 Dr. Tilmann Bubeck <tilmann@bubecks.de> - 0:1.5-1
- update to upstream's xmlunit-1.5

* Fri Sep 27 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.4-4
- Enable test suite
- Resolves: rhbz#987412

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.4-2
- Update to latest packaging guidelines
- Cleanup BuildRequires

* Fri Feb 15 2013 Dr. Tilmann Bubeck <t.bubeck@reinform.de> - 0:1.4-1
- update to upstream's xmlunit-1.4

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 30 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.3-3
- Build javadoc only.

* Thu Dec 30 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.3-2
- BR java 1.6 to prevent gcj failure.

* Thu Dec 30 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.3-1
- Update to new upstream.
- Drop gcj.
- Rebuild docs.

* Thu Mar 11 2010 Peter Lemenkov <lemenkov@gmail.com> - 0:1.0-8.3
- Added missing Requires jpackage-utils

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-8.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.0-6.2
- drop repotag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:1.0-6jpp.1
- Autorebuild for GCC 4.3

* Thu Jan 17 2008 Permaine Cheung <pcheung@redhat.com> - 0:1.0-5jpp.1
- Update to the same version as upstream

 Tue Dec 18 2007 Ralph Apel <r.apel at r-apel.de> - 0:1.0-5jpp
- Add poms and depmap frags
- Make Vendor, Distribution based on macro
- Add gcj_support option

* Mon Mar 12 2007 Permaine Cheung <pcheung@redhat.com> - 0:1.0-4jpp.1
- Add missing BR, patch to build javadoc, and other rpmlint issues

* Mon May 08 2006 Ralph Apel <r.apel at r-apel.de> - 0:1.0-4jpp
- First JPP-1.7 release

* Thu Aug 26 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0-3jpp
- Build with ant-1.6.2

* Wed Dec 17 2003 Paul Nasrat <pauln at truemesh.com> - 0:1.0-2jpp
- Fix license and improved description
- Thanks to Ralph Apel who produced a spec - merged version info

* Wed Dec 17 2003 Paul Nasrat <pauln at truemesh.com> - 0:1.0-1jpp
- Initial Version
