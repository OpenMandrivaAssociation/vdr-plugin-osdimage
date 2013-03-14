
%define plugin	osdimage
%define name	vdr-plugin-%plugin
%define version	0.1.2
%define rel	23

Summary:	VDR plugin: OSD Image Viewer
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://brougs78.vdr-developer.org/vdr.htm
Source:		vdr-%plugin-%version.tar.bz2
Patch1:		http://deela.cc.fh-lippe.de/files/vdr-osdimage/vdr-1.3.18-osdimage-0.1.2.patch
Patch2:		vdr-osdimage-0.1.2-gcc41.patch
Patch3:		osdimage-0.1.2-i18n-1.6.patch
Patch4:		osdimage-pkgconfig.patch
BuildRequires:	vdr-devel >= 1.6.0-7
Requires:	vdr-abi = %vdr_abi
BuildRequires:	imagemagick-devel
BuildRequires:	netpbm-devel

%description
Plugin for VDR that allows viewing pictures on the OSD.

%prep
%setup -q -n %plugin-%version
%patch1 -p4 -b .1318
%patch2 -p0 -b .gcc41
%patch3 -p1
%patch4 -p1
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# directory of pictures (required)
var=PICTURE_DIR
param="-d PICTURE_DIR"
%vdr_plugin_params_end

%build
VDR_PLUGIN_EXTRA_FLAGS="$(pkg-config --cflags ImageMagick++)"
%vdr_plugin_build HAVE_NETPBM=1

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY CREDITS TODO




%changelog
* Thu Jul 15 2010 Funda Wang <fwang@mandriva.org> 0.1.2-22mdv2011.0
+ Revision: 553572
- rebuild

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.2-21mdv2010.0
+ Revision: 401088
- rebuild for new VDR
- adapt for vdr compilation flags handling changes, bump buildrequires

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 0.1.2-20mdv2009.1
+ Revision: 359748
- use pkgconfig for Magick++ libs
- rebuild for new vdr
- use backward-compatible pkg-config call for libmagick

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.1.2-19mdv2009.0
+ Revision: 197956
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.1.2-18mdv2009.0
+ Revision: 197699
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- enable netpbm support
- fix build with recent libMagick

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against new imagemagick libs

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.1.2-16mdv2008.1
+ Revision: 145155
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-15mdv2008.1
+ Revision: 103174
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-14mdv2008.0
+ Revision: 50024
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-13mdv2008.0
+ Revision: 42110
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-12mdv2008.0
+ Revision: 22762
- rebuild for new vdr


* Thu Mar 01 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-11mdv2007.0
+ Revision: 130845
- rebuild for new ImageMagick
- rebuild for new ImageMagick

* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-8mdv2007.1
+ Revision: 90949
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-7mdv2007.1
+ Revision: 74062
- rebuild for new vdr
- Import vdr-plugin-osdimage

* Sat Sep 09 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-6mdv2007.0
- rebuild for new imagemagick

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-2mdv2007.0
- rebuild for new vdr

* Sun Jul 16 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-1mdv2007.0
- initial Mandriva release

