%define  debug_package %{nil}

Summary:        Korora configs for KDE
Name:           korora-settings-kde
Version:        0.10
Release:        2%{?dist}

Group:          System Environment/Base
License:        GPLv3+
Url:            http://kororaproject.org
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  desktop-file-utils
Requires:       coreutils sed util-linux redhat-menus

%description
%{summary}.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

#mkdir -p %{buildroot}%{_datadir}/applications/
#mkdir -p %{buildroot}%{_sysconfdir}/skel/Desktop
#mkdir -p %{buildroot}%{_sysconfdir}/skel/.kde/share/config
mkdir -p %{buildroot}%{_sysconfdir}/skel/.local/share
#mkdir -p %{buildroot}%{_sysconfdir}/skel/.config/autostart
#mkdir -p %{buildroot}/usr/local/share/applications
#mkdir -p %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged
#mkdir -p %{buildroot}%{_libdir}/firefox/browser/defaults/profile
#mkdir -p %{buildroot}%{_sysconfdir}/kde/{env,shutdown}

#desktop-file-install --dir=${RPM_BUILD_ROOT}%{_sysconfdir}/skel/.config/autostart/ syndaemon.desktop
#install -m 0755 %{_builddir}/%{name}-%{version}/gpg-agent-startup.sh %{buildroot}%{_sysconfdir}/kde/env/gpg-agent-shutdown.sh
#install -m 0755 %{_builddir}/%{name}-%{version}/gpg-agent-shutdown.sh %{buildroot}%{_sysconfdir}/kde/shutdown/gpg-agent-shutdown.sh
#install -m 0644 %{_builddir}/%{name}-%{version}/applications/* %{buildroot}/usr/local/share/applications/
#cp -a %{_builddir}/%{name}-%{version}/mimeapps-kde.list %{buildroot}%{_datadir}/applications/
#install -m 0644 %{_builddir}/%{name}-%{version}/applications-korora.menu %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged/applications-korora-kde.menu
#cp -a %{_builddir}/%{name}-%{version}/prefs-kde.js %{buildroot}%{_libdir}/firefox/browser/defaults/profile/prefs-kde.js

#fix KDE logon issue
touch %{buildroot}%{_sysconfdir}/skel/.local/share/user-places.xbel

#fix kdenlive mlt issue
#cat > %{buildroot}%{_sysconfdir}/skel/.kde/share/config/kdenliverc << "EOF"
#[version]
#version=0.8
#EOF

#cd %{buildroot}/
#ln -sf /usr/share/applications/kde4/Help.desktop %{buildroot}/etc/skel/Desktop/Help-kde.desktop
#cd -

%clean
rm -rf %{buildroot}

%pre

%post
#cd %{_datadir}/applications/
#ln -sf mimeapps-kde.list mimeapps.list
#cd %{_libdir}/firefox/browser/defaults/profile/
#ln -sf prefs-kde.js prefs.js

#enable GNOME's PackageKit programs in KDE
#sed -i s/NotShowIn=KDE/#NotShowIn=KDE/ /usr/share/applications/gpk*desktop 2>/dev/null

%postun
# clean up the link on uninstall of this package (not updates though)
#if [ "$1" == "0" ]
#then
#  cd %{_libdir}/firefox/browser/defaults/profile/
#  unlink prefs.js 2>/dev/null
#  cd -
#fi


%files 
%defattr(-,root,root,-)
#%{_datadir}/applications/mimeapps-kde.list
#%{_libdir}/firefox/browser/defaults/profile/prefs-kde.js
#%{_sysconfdir}/xdg/menus/applications-merged/applications-korora-kde.menu
#%{_sysconfdir}/skel/.config/autostart/syndaemon.desktop
%{_sysconfdir}/skel/.local/share/user-places.xbel
#%{_sysconfdir}/skel/.kde/share/config/kdenliverc
#/usr/local/share/applications
#/etc/skel/Desktop/Help-kde.desktop
#%{_sysconfdir}/kde/env/gpg-agent-shutdown.sh
#%{_sysconfdir}/kde/shutdown/gpg-agent-shutdown.sh

%changelog
* Fri Jan 9 2015 Chris Smart <csmart@kororaproject.org> 0.10-2
- Fix: touchpad stops working. Removed syndaemon as KDE built-in settings work now.

* Sat Dec 20 2014 Chris Smart <csmart@kororaproject.org> 0.10-1
- Move Firefox profile to generic package.

* Sat May 3 2014 Chris Smart <csmart@kororaproject.org> 0.8-4
- Update mozilla default profile to support adblock-plus 2.6

* Wed Mar 12 2014 Chris Smart <csmart@kororaproject.org> 0.8-3
- Update mozilla default profile to support adblock-plus 2.5.1

* Thu Oct 24 2013 Chris Smart <csmart@kororaproject.org> 0.8-2
- Remove gpg-agent from kde profile, now upstream in kde-settings

* Thu Oct 24 2013 Chris Smart <csmart@kororaproject.org> 0.8-1
- Add gpg-agent to kde profile

* Thu Sep 26 2013 Chris Smart <csmart@kororaproject.org> 0.7-2
- Update Firefox profile to support newer adblock plus

* Mon Jun 10 2013 Chris Smart <csmart@kororaproject.org> 0.7-1
- Remove help from desktop, going to be launchable from Korora Welcome,
clean up firefox prefs.js link on uninstall of package but not upgrades,
remove mime-apps list, remove old desktop files for overrides.

* Wed May 29 2013 Chris Smart <chris@kororaa.org> 0.6-2
- Build for Korora 19 release, remove application menu as items are sorted by category by default now.

* Thu Oct 25 2012 Chris Smart <chris@kororaa.org> 0.6-1
- Build for Korora 18 release.

* Mon May 21 2012 Chris Smart <chris@kororaa.org> 0.5-1
- Update for Kororaa 17, remove workaround for kdenlive.

* Sun Oct 23 2011 Chris Smart <chris@kororaa.org> 0.4-1
- Fix Firefox profile issue where user changes aren't applied, remove old firefox profile locations, update for Kororaa 16.

* Wed Oct 12 2011 Chris Smart <chris@kororaa.org> 0.3-4
- Fix Kdenlive 0.8 issue with mlt libraries.

* Wed Oct 12 2011 Chris Smart <chris@kororaa.org> 0.3-3
- Link Firefox profile to new location.

* Sun Sep 18 2011 Chris Smart <chris@kororaa.org> 0.3-2
- Work around KDE bug when logging in due to missing user-places.xbel

* Sun Aug 21 2011 Chris Smart <chris@kororaa.org> 0.3-1
- Updated for Firefox 6.

* Wed Aug 3 2011 Chris Smart <chris@kororaa.org> 0.2-4
- Removed Firefox4 desktop entry, not required for F15, added GNOME switching desktop script, overwrite default start page to Firefox default.

* Sat Jul 09 2011 Chris Smart <chris@kororaa.org> 0.2-1
- Update for Firefox 5, built for release 15.

* Wed Apr 27 2011 Chris Smart <chris@kororaa.org> 0.1-5
- Modified to create arch specific packages, to fix firefox prefs issue.

* Mon Apr 25 2011 Chris Smart <chris@kororaa.org> 0.1-3
- Cleaned up KDE application menu.

* Sun Apr 24 2011 Chris Smart <chris@kororaa.org> 0.1-2
Set Firefox to use built-in download manager now that we are not shipping download-statusbar.

* Tue Mar 05 2011 Chris Smart <chris@kororaa.org> 0.1-1
- Initial spec, taken from kororaa-extras

