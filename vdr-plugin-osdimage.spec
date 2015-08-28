%define plugin	osdimage

Summary:	VDR plugin: OSD Image Viewer
Name:		vdr-plugin-%{plugin}
Version:	0.1.2
Release:	26
Group:		Video
License:	GPL
URL:		http://brougs78.vdr-developer.org/vdr.htm
Source:		vdr-%{plugin}-%{version}.tar.bz2
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
%setup -q -n %{plugin}-%{version}
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
%doc README HISTORY CREDITS TODO
