import React, { useEffect, useState } from 'react';
import { axiosReq } from '@/api/axiosDefault';
import ProfileCard from '@/components/Card';

const ProfilePage: React.FC = () => {
  const [profile, setProfile] = useState<any>(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await axiosReq.get('/profiles/2/');
        setProfile(response.data);
      } catch (error) {
        console.error('Error fetching profile data:', error);
      }
    };

    fetchProfile();
  }, []);

  if (!profile) {
    return <div>Loading...</div>;
  }

  return (
    <ProfileCard
      ownerUsername={profile.owner_username}
      name={profile.name}
      profilePictureUrl={profile.profile_picture_url}
      bio={profile.bio}
      website={profile.website}
    />
  );
};

export default ProfilePage;
